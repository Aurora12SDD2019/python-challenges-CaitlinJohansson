name = input('Enter your name: ')
print('Your name is ' + name)
age = int(input('Enter your age: '))
year = int(input('Enter your year of birth: '))
while age != 100:
    age += 1

if age == 100:
    year = year + age
    print('You will turn 100 in: ' + str(year))
    
    