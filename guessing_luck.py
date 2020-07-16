import random
print('***Welcome to guessing ur luck with five attempt***')
my_number = random.randint(0, 10)
print(my_number)
total=5
while True:

    x=int(input('\nEnter number from 1 to 10 :'))
    total = total - 1
    if x == my_number :
        print('hurry! you guessed correct number in attempt :', 5-total)
    elif total == 0:
        print('\n**game over**')
    else:
        print('oops! wrong guess,remaining guess', total )
    if x == my_number or total == 0:
        z = input("\nplay agin? Enter 'y' or 'n' :")
        if z[0].lower() == 'y':
            my_number = random.randrange(0, 10)
            total = 5
        else:
            break
# print('your number was :',rand)




