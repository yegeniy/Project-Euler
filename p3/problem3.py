import sys
import math

class ProblemThree:

  def __init__(self):
    self.knownPrimes = [2]

  def largestPrimeFactor(self, n):
    maximum = n #int(math.floor(math.sqrt(n)))
    # print maximum
    for divisor in self.findFactors(n, 2, maximum+1):
      dividend = n/divisor
      print "divisor:", divisor,"; dividend:", dividend
      # print "largestPrimeFactor(",n,"). Dividend: ", dividend
      if self.isPrime(dividend):
        return dividend

  def isPrime(self, n):
    for p in self.calcPrimes(int(math.floor(math.sqrt(n)))):
      # print "isPrime(",n,"): ", p
      if p>=n:
        return True
      if n % p == 0:
        return False
    return True

  def calcPrimes(self, ceiling):
    # returns a list of known primes up to and including ceiling
    for p in self.knownPrimes:
      yield p
    for x in xrange(self.knownPrimes[len(self.knownPrimes)-1]+1, ceiling+1):
      isPrime = True
      for p in self.knownPrimes:
        # print p, x
        # TODO: List Comprehension
        # if p < int(math.floor(math.sqrt(x))):
          if x % p == 0:
            # print x, " divisible by ", p
            isPrime = False
            break
      if isPrime:
        self.knownPrimes.append(x)
        yield x

  def findFactors(self, n, start, end):
    for x in xrange(start, end):
      if n%x == 0:
        yield x

if __name__ == '__main__':
  problem3 = ProblemThree()
  n = int(sys.argv[1])
  print problem3.largestPrimeFactor(n)