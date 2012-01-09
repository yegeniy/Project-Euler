import sys

class ProblemNine:
  def pythagoreanTriple(self, total):
    a = 1
    b = a+1
    c = total - (b + a)
    while a < b:
      b = a + 1
      c = total - (b + a)
      while b < c:
        if a**2 + b**2 == c**2:
          return a,b,c
        b+=1
        c-=1
      a+=1

if __name__ == '__main__':
  problem9 = ProblemNine()
  n = int(sys.argv[1])
  a,b,c = problem9.pythagoreanTriple(n)
  print a,"*",b,"*",c,"=",a*b*c