import unittest
from tests.home.login_test_csv_data import LoginTestWithCSVData

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTestWithCSVData)
#tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)