'''
Created on Sep 21, 2009

@author: rsvihla
'''
import reports as r
import output as o
import client as cl
from ttypes import *
from thrift.Thrift import TApplicationException
from thread import get_ident
from threading import Thread, Lock
import time
from random import randint, gauss
from hashlib import md5
import time

#need to make this configurable. Jonathan's default was 1000**2
TOTAL_KEYS = 10**2

COLUMNS_PER_KEY = 5

# a generator that generates all keys according to a bell curve centered
# around the middle of the keys generated (0..TOTAL_KEYS).  Remember that
# about 68% of keys will be within STDEV away from the mean and 
# about 95% within 2*STDEV.
STDEV = 3000
MEAN = TOTAL_KEYS / 2
def key_generator():
    while True:
        guess = gauss(MEAN, STDEV)
        if 0 <= guess < TOTAL_KEYS:
            return guess

detailsLock = Lock()


def addetails(details, record):
    detailsLock.acquire()
    details.append(record)
    detailsLock.release()
    
    
class Inserter(Thread):
    def __init__(self, i, server, port, details,threadcount):
        Thread.__init__(self)
        KEYS_PER_THREAD = TOTAL_KEYS / threadcount
        self.range = xrange(KEYS_PER_THREAD * i, KEYS_PER_THREAD * (i + 1))
        self.server = server
        self.port = port
        self.details = details

    def run(self):
        client = cl.client_connect(self.server,self.port)
        client.transport.open()
        data = md5(str(get_ident())).hexdigest()
        columns = [Column(chr(ord('A') + j), data, 0) for j in xrange(COLUMNS_PER_KEY)]
        self.count = 0
        starttime = time.time()
        for i in self.range:
            key = str(i)
            cfmap = {'Standard1': [ColumnOrSuperColumn(column=c) for c in columns]}
            client.batch_insert('Keyspace1', key, cfmap, ConsistencyLevel.ONE)
            self.count += 1
        endtime = time.time()
        timeelapsed = endtime - starttime
        addetails(self.details,("writing", self.count,timeelapsed ))
        
class Reader(Thread):
    
    def __init__(self, server, port,details,threadcount):
        Thread.__init__(self)
        self.keysperthread = TOTAL_KEYS / threadcount
        self.server = server
        self.port = port
        self.details = details
        
    def run(self):
        client = cl.client_connect(self.server,self.port)
        client.transport.open()
        starttime = time.time()
        parent = ColumnParent('Standard1')
        p = SlicePredicate(slice_range=SliceRange('', '', False, COLUMNS_PER_KEY))
        for self.count in xrange(self.keysperthread+1):
            key = str(key_generator())
            client.get_slice('Keyspace1', key, parent, p, ConsistencyLevel.ONE)
        endtime = time.time()
        addetails(self.details, ("reading", self.count, endtime- starttime))

def insert(ip, port,threadcount):
    detail = []
    threads = []
    for i in xrange(threadcount):
        th = Inserter(i,ip, port, detail,threadcount)
        threads.append(th)
        th.start()
    while [th for th in threads if th.isAlive()]:
        time.sleep(10)
    return detail
    
def read(ip, port,threadcount):
    detail = []
    threads = []
    for i in xrange(threadcount):
        th = Reader(ip, port, detail,threadcount)
        threads.append(th)
        th.start()
    while [th for th in threads if th.isAlive()]:
        time.sleep(10)
    return detail
    
def benchme(threadcount,server):
    host = (server.split(":"))
    insertdetails = insert(host[0], int(host[1]), threadcount)
    readdetails = read(host[0], int(host[1]),threadcount)
    return insertdetails + readdetails
    #return insertdetails
    
    

def run(server, threads, reporttype, outputname):
    details = benchme(threads,server)
    report= r.Reports(details)
    o.consoleout(report)
    #print filter(lambda x:x == reporttype, dir(o))[0]

# .__init__().save(outputname)

if __name__ == '__main__':
    filetype = "Html"
    filename = "output.html"
    run(50,filetype, filename)