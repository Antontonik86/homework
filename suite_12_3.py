import test_12_3
import unittest
import inspect

test_suit = unittest.TestSuite()
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suit)