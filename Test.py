import unittest
from IPtracker import IPtracker

# Class to conduct unit testing on IP tracker
class IPTestCase(unittest.TestCase):
    # Function to write test cases
    def testIPtracker(self):
        IP_object = IPtracker()

        # Test 1: Populating the cache with IP addresses using request_handled
        for i in range(200):
            IP_object.request_handled("145.87.2.109")

        for i in range(100):
            IP_object.request_handled("91.66.12.187")

        for i in range(10):
            IP_object.request_handled("124.31.76.142")

        IP_object.request_handled("16.121.46.12")

        # Test case 2: To test top100 function of IPtracker
        result = IP_object.top100()
        expected = ['145.87.2.109', '91.66.12.187', '124.31.76.142', '16.121.46.12']
        self.assertEqual(result, expected)

        # Test case 3: To test clear function of IPtracker
        IP_object.clear()
        result = IP_object.top100()
        expected = []
        self.assertEqual(result, expected)

        print("All test cases passed")

IPTestCaseObj = IPTestCase()
IPTestCaseObj.testIPtracker()
