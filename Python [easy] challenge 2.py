num = int(input('Enter a number: '))
divide = num % 2
if divide == 0:
    print('Your number, ' + str(num) + ', is an even number.')
else:
    print('Your number, ' + str(num) + ', is an odd number.')