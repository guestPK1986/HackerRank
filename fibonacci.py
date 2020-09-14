#Write a function that returns fibonacci sequence of number N.

def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    temp = a
    a = b
    b = temp + b


for x in fib(21):
  print(x)