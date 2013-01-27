""" Project Euler Problem 6

The difference between the sum of the squares of the first ten natural numbers and the square of
the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
"""
squares = 0
sums = 0
for i in xrange(1,101):
  squares += i*i
  sums += i
print sums * sums - squares
