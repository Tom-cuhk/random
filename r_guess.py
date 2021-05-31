# random number
# import
# guess the number
import random
print('Please set the range of the number')
s = input('The lower number is :')
s = int(s)
l = input('The upper number is :')
l = int(l)
r = random.randint(s, l)	
count = 1
x = input('Please input a number: ')
x = int(x)
while x < s or x > l:
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
	x = int(input('Please input a number between: '))
	


