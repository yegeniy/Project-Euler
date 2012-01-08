import unittest
from problem3 import ProblemThree

class TestProblem(unittest.TestCase):

  def test_(self):
    problem3 = ProblemThree()
    self.assertEqual(29, problem3.largestPrimeFactor(13195))
    self.assertEqual(5, problem3.largestPrimeFactor(5))

if __name__ == '__main__':
    unittest.main()