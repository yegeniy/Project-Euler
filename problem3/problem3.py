import sys

class ProblemThree:

  def largestPrimeFactor(self, n):

    for factor in self.findFactors(n):
      if factor == 1:
        return n
      if self.isPrime(factor):
        return factor

  def findFactors(self,n):
    for x in range(n/2, 1, -1):
      while n%x != 0 and x > 1:
        x -= 1
      yield x

  def findFactor(self, n):
    divisor = n/2
    while n%divisor != 0 and divisor > 1:
      divisor -= 1
    return divisor

  def isPrime(self, factor):
    return self.findFactors(factor).next() == 1


if __name__ == '__main__':
  problem3 = ProblemThree()
  n = int(sys.argv[1])
  print problem3.largestPrimeFactor(n)