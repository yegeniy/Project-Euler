import sys

class ProblemOne:
  def sumMultiples(self, n):
    sum = 0
    for x in xrange(1,n):
      if self.divisibleBy(x, (3,5)):
        sum += x
    return sum

  def divisibleBy(self, x, divisors):
    for d in divisors:
      if x%d == 0:
        return True

if __name__ == '__main__':
  p1 = ProblemOne()
  n = int(sys.argv[1])
  print p1.sumMultiples(n)