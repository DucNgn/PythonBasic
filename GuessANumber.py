import random
target = random.randint(1, 20)

for guess in range(0, 7):
    print('Guess the number in range 1 to 20')
    keyIn = int(input())

    if(keyIn == target):
        print('Congratulation')
        print('The right answer was ' + str(target))
        break
    elif(keyIn > target):
        print('You are guessing too high')
    else:
        print('You are guessing too low')

print('End of program')
