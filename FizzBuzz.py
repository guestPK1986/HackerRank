#FizzBuzz
#Write a program that prints each number from 1 to n on a new line. constraints 0<n<2*(10**5)
#For each multiple of 3, print "Fizz" instead of the number. 
#For each multiple of 5, print "Buzz" instead of the number. 
#For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
#Otherwise print number.

def fizzBuzz(n):
    if i % 3 == 0 and i%5 ==0:
        return('FizzBuzz')
    if i % 3 == 0:
        return('Fizz')
    if i % 5 == 0:
        return('Buzz')
    else:
        return(i)

n = int(input().strip())
for i in range(1,n+1):
    if 0< n and n < 2*(10**5):
        print(fizzBuzz(n))
