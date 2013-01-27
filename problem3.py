""" Project Euler Problem 3

What is the largest prime factor of the number 600851475143 ?

"""
num = 600851475143
factor = num
n = 1
while n * n < num:
  if factor % n == 0 :
    factor = factor / n
    answer = n
  n += 1
print answer

