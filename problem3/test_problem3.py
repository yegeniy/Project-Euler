import unittest
from problem3 import ProblemThree

class TestProblem(unittest.TestCase):

  def setUp(self):
    self.problem3 = ProblemThree()

  def test_largestPrimeFactor(self):
    self.assertEqual(29, self.problem3.largestPrimeFactor(13195))
    self.assertEqual(5, self.problem3.largestPrimeFactor(5))

  def test_isPrime(self):
    self.assertFalse(self.problem3.isPrime(4))
    self.assertTrue(self.problem3.isPrime(29))
    self.assertTrue(self.problem3.isPrime(5))
    self.assertTrue(self.problem3.isPrime(2))


  def test_calcPrimes(self):
    self.assertEqual([2], list(self.problem3.calcPrimes(2)))
    self.assertEqual([2,3], list(self.problem3.calcPrimes(3)))
    self.assertEqual([2,3,5], list(self.problem3.calcPrimes(6)))
    self.assertEqual([2,3,5,7,11,13,17,19,23,29], list(self.problem3.calcPrimes(29)))
    # print len(list(self.problem3.calcPrimes(775146)))

if __name__ == '__main__':
    unittest.main()