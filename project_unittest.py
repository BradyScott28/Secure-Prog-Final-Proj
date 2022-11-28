import unittest
from ScottBMod2Project import ppeusage, averageusage, ppeleft, daysleft

class ppetests(unittest.TestCase):
    def test_ppeusage(self):
        tc = ppeusage(8, 10)
        self.assertEqual(tc, 2)
        
    def test_averageusage(self):
        avg = averageusage(8, 4)
        self.assertEqual(avg, 2)
        
    def test_ppeleft(self):
        pperemain = ppeleft(4)
        self.assertEqual(pperemain, 800)
        
    def test_daysleft(self):
        daysRemain = daysleft(4, 2)
        self.assertEqual(daysRemain, 2)
        
if __name__ == '__main__':
    unittest.main( )