import random 
print("Let's play a game in which you have to guess the no. which I am thinking about. Also remember you can only try for 5 times.")
_no = random.randint(1,50)
print("I am thinking about a number(It is upto 100.)")
for a in range(1,6):
    print("Take the guess.")
    global guess
    guess = int(input('>'))
    if guess < _no:
        print('Your guess is too low.')
    elif guess > _no:
        print('Your guess is too high.')
    else:
        break  

if guess == _no:
    print('Good job! You got it in ' + str(a) + ' guesses!')
else:
    print('Nope, The number was ' + str(_no))
