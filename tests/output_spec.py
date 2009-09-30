'''
Created on Sep 24, 2009

@author: rsvihla
'''
import unittest
import cassandrabench.output as o
import cassandrabench.reports as r    
    
def _contextsetup(details):
    details.append(("writing", 1100, 1))
    details.append(("reading", 600, 2))
    return r.Reports(details)

class TestHtmlOutput(unittest.TestCase):

    def _assertContains(self, compare, num):
        self.assertEqual(self.html.output.count(str(compare)), num)
         
    def setUp(self):
        self.rep = _contextsetup([])
        self.html = o.Html(self.rep)
        
        
    def test_should_display_all_report_details(self):
        self._assertContains("<td>writing</td><td>1100</td><td>1</td>", 1)
        self._assertContains("<td>reading</td><td>600</td><td>2</td>", 1)
        
    def test_should_contain_mean_rps_and_mean_rps(self):
        self._assertContains("<td>mean wps</td><td>1100.0</td>", 1)
        self._assertContains("<td>mean rps</td><td>300.0</td>", 1)
        
    def test_should_contain_max_rps_and_max_rps(self):
        self._assertContains("<td>max wps</td><td>1100.0</td>", 1)
        self._assertContains("<td>max rps</td><td>300.0</td>", 1)  
        
    def test_should_contain_min_rps_and_min_rps(self):
        self._assertContains("<td>min wps</td><td>1100.0</td>", 1)
        self._assertContains("<td>min rps</td><td>300.0</td>", 1)
        
    def test_should_contain_total_read_time_and_total_write_time(self):
        self._assertContains("<td>total read time</td><td>2</td>", 1)
        self._assertContains("<td>total write time</td><td>1</td>", 1)       
        
    def test_should_contain_median_rps_and_median_wps(self):
        self._assertContains("<td>median rps</td><td>300.0</td>", 1)
        self._assertContains("<td>median wps</td><td>1100.0</td>", 1)       
                         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()