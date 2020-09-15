#Write a program that generates a number 1~10. Gets input from user
#Checks that input is a number 1~10
#Check if randomly generated number is equals to user's guess


from random import randint
answer = randint(1, 10)

while True:
    try:
        guess = int(input('guess a number 1~10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
            print('please enter a number 1~10')
            continue
