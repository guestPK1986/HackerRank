# Given an n integer, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20, print Not Weird
# Print Weird if the number is weird. Otherwise, print Not Weird.

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 !=0:
        print('Weird')
    elif n%2==0 and n in range (2,6):
        print('Not Weird')
    elif n%2==0 and n in range (6,21):
        print('Weird')
    elif n%2==0 and n > 20:
        print('Not Weird')
    else:
        print('Not Weird')

#OR

n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}
print(check[n%2==0 and (n in range(2,6) or n > 20)])
