'''
Created on Sep 22, 2009

@author: rsvihla
'''

class BaseOutPut(object):
    '''
    classdocs
    '''
    def __init__(self, report):
        self.report = report
        
    @property
    def output(self):
        pass
    
    def save(self, filename):
        f = open(filename)
        f.write(self.output)
    
class Html(BaseOutPut):
    
    @property
    def output(self):
        html = []
        html.append( "<html>")
        html.append("<head/>")
        html.append("<body>details")
        html.append("<table>")
        html.append("<tr><td>measurement</td><td>stats</td>")
        html.append( self._writemeasure("mean wps", self.report.avg_wps ))
        html.append( self._writemeasure("mean rps", self.report.avg_rps ))
        html.append( self._writemeasure("median wps", self.report.med_wps ))
        html.append( self._writemeasure("median rps", self.report.med_rps ))
        html.append( self._writemeasure("max wps", self.report.max_wps ))
        html.append( self._writemeasure("max rps", self.report.max_rps ))
        html.append( self._writemeasure("min wps", self.report.min_wps ))
        html.append( self._writemeasure("min rps", self.report.min_rps ))
        html.append( self._writemeasure("total read time", self.report.total_read_time ))
        html.append( self._writemeasure("total write time", self.report.total_write_time ))
        html.append( "</table>")
        html.append( "<table>")
        html.append("<tr><td>detail</td><td></td><td></td><td></td></tr>")
        for w in self.report.written:
            html.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (w.name, w.records, w.time, w.persec))
        for w in self.report.read:
            html.append( "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (w.name, w.records, w.time, w.persec))
        html.append("</table>")
        return '\n'.join(html)
        
    def _writemeasure(self, measure, data):
        return "<tr><td>%s</td><td>%s</td></tr>" % (measure, data) 
    
class Xml(BaseOutPut):
    pass
