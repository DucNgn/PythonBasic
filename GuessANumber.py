import random
target = random.randint(1, 20)
print('The system chose a random number ! Now it is your turn:')

for guess in range(0, 5):
    print('Guess a number in range 1 to 20')
    keyIn = int(input())

    if(keyIn == target):
        print('Congratulation')
        print('The right answer was ' + str(target))
        exit(0)
    elif(keyIn > target):
        print('You are guessing too high')
    else:
        print('You are guessing too low')

print('You lose!!')

