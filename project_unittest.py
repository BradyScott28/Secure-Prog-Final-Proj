import unittest
from ScottBMos2Project import ppeusage, averageusage, ppeleft, daysleft

class ppetests(unittest.TestCase):
    def test_ppeusage(self):
        totalcount = ppeusage(8, 10)
        self.assertEquals(totalcount, 2)
        
    def test_averageusage(self):
        average = averageusage(8, 4)
        self.assertEquals(average, 2)
        
    def test_ppeleft(self):
        ppeleft = ppeleft(4)
        self.assertEquals(ppeleft, 800)
        
    def test_daysleft(self):
        dayslest = daysleft(4, 2)
        self.assertEquals(sdaysleft, 2)
        
if __name__ == '__main__':
    unittest.main( )