""" Project Euler Problem 7

What is the 10001st prime number?
"""
import time

def isPrime(val, primes):
  for prime in primes:
    if prime * prime > val:
      return True
      break
    elif val % prime == 0:
      return False
      break

start = time.time()
primelist = [2]
for i in xrange(3, 1000000, 2): #increment by 2 to test only odd numbers
  if len(primelist) == 10001:
    print primelist[-1], time.time() - start
    break
  elif isPrime(i, primelist):
    primelist.append(i)
else:
  print "the 10001st prime is not in this range"

