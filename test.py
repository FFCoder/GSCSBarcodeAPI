import unittest
import processors

class TestProcessors(unittest.TestCase):
    def testIfPDFisReturned(self):
        pass
    def testIfXlsLoads(self):
        testItem = processors.writeLabels('export.xlsx',None,None)
        self.assertTrue(testItem)
if __name__ == '__main__':
    unittest.main()