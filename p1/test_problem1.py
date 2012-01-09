import unittest
from problem1 import ProblemOne

class TestProblemOne(unittest.TestCase):

  def test_sumMultiples(self):
    problem1 = ProblemOne()
    self.assertEqual(23, problem1.sumMultiples(10))
    self.assertEqual(0,  problem1.sumMultiples(3))
    self.assertEqual(3,  problem1.sumMultiples(5))

if __name__ == '__main__':
    unittest.main()