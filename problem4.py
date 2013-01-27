""" Project Euler Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

def isPalindrome(value):
  val = str(value)
  return val == val[::-1]

def products(m, n):
  while n > 900:
    if isPalindrome(m * n):
      return m * n
      break
    n = n - 1

#start = time.time()
x = 1000
while x > 900:
  y = x
  if products(y, x):
    print products(y, x)
    #print time.time() - start
    break
  x = x - 1
