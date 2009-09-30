'''
Created on Sep 21, 2009

@author: rsvihla
'''

def _median(type):
    numbers = map(lambda x:x.persec, type)
    n = len(numbers)
    copy = numbers[:] # So that "numbers" keeps its original order
    copy.sort()
    if n & 1:         # There is an odd number of elements
        return round(copy[n // 2],2)
    else:
        return round(((copy[n // 2 - 1] + copy[n // 2]) / 2),2)
  
def _min(type):
        return round(min(map(lambda x:x.persec, type)),2)  
           
def _max(type):
    return round(max(map(lambda x:x.persec, type)),2)

def sumtotaltime( type):
    return sum(map(lambda x:x.time, type))

def sumtotalrecords( type):
    recordlist = map(lambda x: x.records, type)
    return sum(recordlist)

def _avg( type):
    sumtime= sumtotaltime(type)
    sumrecords = sumtotalrecords(type) 
    return round(sumrecords/sumtime,2)

class ReportDetail(object):
    
    def __init__(self, tple):
        self.tple = tple
        
    @property
    def persec(self):
        return self.tple[1]/self.tple[2]
    
    @property
    def records(self):
        return self.tple[1]
    
    @property
    def time(self):
        return self.tple[2]
    
    @property
    def name(self):
        return self.tple[0]
    
class Reports(object):
    
    def __init__(self, details):
        details = [ReportDetail(tpl) for tpl in details]
        self._readers =filter(lambda x:x.name=="reading", details)
        self._writers = filter(lambda x:x.name=="writing", details)
        
    @property
    def written(self):
        return self._writers
    
    @property
    def read(self):
        return self._readers
    
    @property
    def total_reads(self):
        return sumtotalrecords(self._readers)
    
    @property
    def total_writes(self):
        return sumtotalrecords(self._writers)
    
    @property
    def total_read_time(self):
        return sumtotaltime(self._readers)
    
    @property
    def total_write_time(self):
        return sumtotaltime(self._writers)
    
    @property
    def min_rps(self):
        return _min(self._readers)
      
    @property
    def max_rps(self):
        return _max(self._readers)
    @property
    def med_rps(self):
        return _median(self._readers)
    
    @property
    def med_wps(self):
        return _median(self._writers)
    
    @property
    def avg_rps(self):
        return _avg(self._readers)
    
    @property
    def min_wps(self):
        return _min(self._writers)
    
    @property
    def max_wps(self):
        return _max(self._writers)
   
    @property
    def avg_wps(self):
        return _avg(self._writers)
    
    
        