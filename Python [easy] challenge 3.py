a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = int(input('Enter a number: '))
for i in a:
   if i < c:
        b.append(i)
print(c)
print(b)    