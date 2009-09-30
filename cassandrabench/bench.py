'''
Created on Sep 21, 2009

@author: rsvihla
'''
import reports as r
import output as o

def benchme(threads):
    detail = []
    detail.append(("writing", 1000, 2.67)) # 374.53 wps
    detail.append(("writing", 1200, 2.24)) # 535.71 wps
    detail.append(("writing", 1100, 2.50)) # 440.00 wps
    detail.append(("reading", 1000, 1.11)) # 900.90 rps
    detail.append(("reading", 1200, 1.82)) # 659.34 rps
    detail.append(("reading", 1100, 1.23)) # 894.31 rps
    return detail

def consoleout(reportdata):
    print "average reads per sec are " + str(reportdata.avg_rps )
    print "average writes per sec are " + str(reportdata.avg_wps )

def run(threads, reporttype, outputname):
    details = benchme(threads)
    report= r.Reports(details)
    consoleout(report)
    print filter(lambda x:x == reporttype, dir(o))[0]

# .__init__().save(outputname)

if __name__ == '__main__':
    filetype = "Html"
    filename = "output.html"
    run(50,filetype, filename)