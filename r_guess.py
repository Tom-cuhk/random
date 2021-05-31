# random number
# import
# guess the number
import random
r = random.randint(1, 20)	
count = 1
x = int(input('Please input a number between 1 - 20: '))
while x < 1 or x > 20:
	x = int(input('Please input the number again: '))
while True:

	if x == r:
		print('You have the corrent number!' , ' You have tried', count, 'times')
		break
	elif x < r:
		print('Your number is smaller than the answer', ', you have tried', count, 'times')
		count = count + 1
	elif x > r:
		print('Your number is greater than the answer', ', you have tried', count, 'times')
		count = count + 1
	x = int(input('Please input a number between 1 - 20: '))


