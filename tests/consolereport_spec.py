'''
Created on Sep 21, 2009

@author: rsvihla
'''
import unittest
import cassandrabench.reports as r

class TestReporter(unittest.TestCase):


    def setUp(self):
        detail = []
        detail.append(("writing", 1000, 2.67)) # 374.53 wps
        detail.append(("writing", 1200, 2.24)) # 535.71 wps
        detail.append(("writing", 1100, 2.50)) # 440.00 wps
        detail.append(("reading", 1000, 1.11)) # 900.90 rps
        detail.append(("reading", 1200, 1.82)) # 659.34 rps
        detail.append(("reading", 1100, 1.23)) # 894.31 rps
        self.report = r.Reports(detail)

    def test_should_provide_per_sec_count_for_each_detail_item(self):
        self.assertAlmostEqual( self.report.written[0].persec , 1000/2.67)
        self.assertAlmostEqual(self.report.written[1].persec , 1200/2.24)
        self.assertAlmostEqual(self.report.read[2].persec , 1100/1.23)

    def test_should_provide_total_reads(self):
        self.assertAlmostEqual(self.report.total_reads , 3300)
    
    def test_should_provide_total_time_for_reads(self):
        self.assertAlmostEqual (self.report.total_read_time , 1.11+1.82+1.23)
    
    def test_should_provide_total_writes(self):
        self.assertAlmostEqual (self.report.total_writes, 3300)
    
    def test_should_provide_total_time_for_writes(self):
        self.assertAlmostEqual(self.report.total_write_time, 2.67+2.24+2.50)
    
    def test_should_provide_average_reads_per_sec(self):
        self.assertAlmostEqual(self.report.avg_rps, round(3300/(1.11+1.82+1.23),2))
    
    def test_should_provide_average_writes_per_sec(self):
        self.assertAlmostEqual(self.report.avg_wps, round(3300/(2.67+2.24+2.50),2))
    
    def test_should_provide_median_writes_per_sec(self):
        self.assertAlmostEqual(self.report.med_wps, 440.00 )
        
    def test_should_provide_median_reads_per_sec(self):
        self.assertAlmostEqual(self.report.med_rps, 894.31 )
    
    def test_should_provide_max_writes_per_sec(self):
        self.assertAlmostEqual(self.report.max_wps, 535.71)
    
    def test_should_provide_min_writes_per_sec(self):
        self.assertAlmostEqual(self.report.min_wps, 374.53)
    
    def test_should_provide_max_reads_per_sec(self):
        self.assertAlmostEqual(self.report.max_rps, 900.90)
    
    def test_should_provide_min_reads_per_sec(self):
        self.assertAlmostEqual(self.report.min_rps, 659.34)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()