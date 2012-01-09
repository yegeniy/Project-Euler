import unittest
from problem9 import ProblemNine

class TestProblem(unittest.TestCase):

  def test_pythagoreanTriple(self):
    problem9 = ProblemNine()
    self.assertEqual((3,4,5), problem9.pythagoreanTriple(3+4+5))

if __name__ == '__main__':
    unittest.main()