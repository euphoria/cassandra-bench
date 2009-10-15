'''
Created on Sep 22, 2009

@author: rsvihla
'''
import types
import reports as r

def _getproperties(o):
    props = [(prop, getattr(o,prop)) for prop in dir(o) if not isinstance(getattr(o,prop), types.MethodType) and not prop.startswith('_')]
    return props

def _detailoutput(details):
    print "--------------------"
    print "name | records | time | persec"
    for det in details:
        record = "%s | %s | %s | %s" % (det.name ,str(det.records) , str(det.time) , str(det.persec))
        print record
    print "--------------------"
       
def consoleout(reports):
    print "benchmarking complete"
    print "summary below"
    print "--------------------"
    for reportdata in reports:
        print "___host : " + reportdata.host + "-------------------"
        props = _getproperties(reportdata)
        for p in props:
            if not p[0] == "written" and not p[0] == "read" and not p[0] == "host": 
                print str(p[0]) + ":"+ str(p[1])
                print "--------------------"
        print "details below"
        written = [p[1] for p in props if p[0] == "written"][0]
        read = [p[1] for p in props if p[0] == "read"][0]   
        print "written details"
        _detailoutput(written)
        print "read details"
        _detailoutput(read)
        print "-------------end host-----------------"
            

    
class Html(object):
    
    
    def output(self,reports):
        html = []
        html.append( "<html>")
        html.append("<head/>")
        html.append("<body>details")
        for r in reports:
            html.append("<h2>"+str(r.host)+"</h2>")
            html.append("<table>")
            html.append("<tr><td>measurement</td><td>stats</td>")
            html.append( self._writemeasure("mean wps", r.avg_wps ))
            html.append( self._writemeasure("mean rps", r.avg_rps ))
            html.append( self._writemeasure("median wps", r.med_wps ))
            html.append( self._writemeasure("median rps", r.med_rps ))
            html.append( self._writemeasure("max wps", r.max_wps ))
            html.append( self._writemeasure("max rps", r.max_rps ))
            html.append( self._writemeasure("min wps", r.min_wps ))
            html.append( self._writemeasure("min rps", r.min_rps ))
            html.append( self._writemeasure("total read time", r.total_read_time ))
            html.append( self._writemeasure("total write time", r.total_write_time ))
            html.append( "</table>")
            html.append( "<table>")
            html.append("<tr><td>detail</td><td></td><td></td><td></td></tr>")
            for w in r.written:
                html.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (w.name, w.records, w.time, w.persec))
            for w in r.read:
                html.append( "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (w.name, w.records, w.time, w.persec))
            html.append("</table>")
        html.append("</body>")
        html.append("</html>")
        return '\n'.join(html)
        
    def _writemeasure(self, measure, data):
        return "<tr><td>%s</td><td>%s</td></tr>" % (measure, data) 
    






