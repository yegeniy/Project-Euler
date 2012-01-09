import sys

class ProblemTwo:

  def sumEvenFibonacci(self, maximum):
    if(maximum < 2):
      return 0
    else:
      sum = 2
      self.fib = FibonacciGenerator()
      # if backOne is >= maximum, then the next number is higher
      for x in self.fib.generateSeq(maximum):
        if x%2==0:
          sum += x
      return sum

class FibonacciGenerator:

  def __init__(self, backTwo=1, backOne=2):
    self.backTwo = backTwo
    self.backOne = backOne

  def generateSeq(self, maximum):
    while True:
      next = self.backTwo + self.backOne
      if (next <= maximum):
        yield next
        self.backTwo = self.backOne
        self.backOne = next
      else:
        break

if __name__ == '__main__':
  p2 = ProblemTwo()
  n = int(sys.argv[1])
  print p2.sumEvenFibonacci(n)