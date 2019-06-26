num = int(input('Enter a number: '))
divider = int(input('Enter a number to divide your number by: '))
range = list(range(1, divider+1))
dividelist = []
for dividers in range:
    if divider % dividers == 0:
        dividelist.append(dividers)
print(dividelist)