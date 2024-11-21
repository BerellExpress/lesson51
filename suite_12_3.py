import unittest
from RunnerTest import RunnerTest
from tests_12_3 import TournamentTest

test_suite = unittest.TestSuite()
runner_test = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
test_suite.addTest(runner_test)

tournament_tests = unittest.TestLoader().loadTestsFromTestCase(TournamentTest)
test_suite.addTest(tournament_tests)

runner = unittest.TextTestRunner(verbosity=2)

results = runner.run(test_suite)