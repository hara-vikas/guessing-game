import random
GEN = random.randint(1, 100)
print('hello welcome to the world of guesses')
print('here the rules of game')                          #rules of the game and notes of it
print('enter the guesses within 1 to 100 numbers')
print('if you are near to the number within 10 numbers it shows -warm')
print('if you are near to the number away 10 numbers it shows - cold')
print('if you are very near to the number it shows - warmer')
print('if you are farther than the number before it shows -colder', '\nlets start')
ALGUESS, PREGUESS, FLAG = 0, 0, 0
while True:                                                        #while loop for iteratons
   if FLAG == 1:
       PREGUESS = GUESS
	
   GUESS = int(input('enter your guess'))
   ALGUESS = ALGUESS+1
   if GUESS in range(1, 101):
       if GUESS == GEN:
	   print('congrats your guess is correct')         #if statements for checking conditions
	   print("number of guesses", ALGUESS)
	   exit()
       elif abs(GEN-GUESS) <= 10 and GEN > GUESS and FLAG == 0:
	   FLAG = 1
	   print('warm')
	   continue
       elif abs(GEN-GUESS) <= 10 and GEN < GUESS and FLAG == 0:
	   FLAG = 1
	   print('cold')
	   continue
       elif abs(GEN-GUESS) < abs(GEN-PREGUESS) and FLAG == 1:
	   print('warmer')
	   continue
       elif abs(GEN-GUESS) > abs(GEN-PREGUESS) and FLAG == 1:
	   print('colder')
	   continue
   else:
       print('out of bounds')
       print('number should lie between 1 to 100')
