import random
gen=random.randint(1,100)
print('hello welcome to the world of guesses')
print('some of the rules of game')                          #rules of the game and notes of it
print('enter the guesses within 1 to 100 numbers')
print('if you are near to the number within 10 numbers it shows -warm')
print('if you are near to the number away 10 numbers it shows - cold')
print('if you are very near to the number it shows - warmer')
print('if you are farther than the number before it shows -colder','\nlets start')
alguess,preguess,flag=0,0,0
while True:                                                        #while loop for iteratons
	if flag==1:
		preguess=guess                                
	guess=int(input('enter your guess'))
	alguess=alguess+1
	if guess in range(1,101):
		if guess==gen:
			print('congrats your guess is correct')         #if statements for checking conditions
			print("number of guesses",alguess)
			exit()
		elif abs(gen-guess)<=10 and gen>guess and flag==0:
			flag=1
			print('warm')
			continue
		elif abs(gen-guess)<=10 and gen<guess and flag==0:
			flag=1
			print('cold')
			continue
		elif abs(gen-guess)<abs(gen-preguess) and flag==1:
			print('warmer')
			continue
		elif abs(gen-guess)>abs(gen-preguess) and flag==1:
			print('colder')
			continue
	else:
		print('out of bounds')
		print('number should lie between 1 to 100')