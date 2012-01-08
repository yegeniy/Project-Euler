import unittest
from problem2 import ProblemTwo

class TestProblem(unittest.TestCase):

  def test_sumEvenFibonacci(self):
    problem2 = ProblemTwo()
    # First few terms of Fibonacci seq: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    self.assertEquals(10, problem2.sumEvenFibonacci(30))
    self.assertEquals(44, problem2.sumEvenFibonacci(34))
    self.assertEquals(44, problem2.sumEvenFibonacci(35))
    self.assertEquals(2, problem2.sumEvenFibonacci(2))

if __name__ == '__main__':
    unittest.main()