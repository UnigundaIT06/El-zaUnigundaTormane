a = int(input('Ievadiet skaitli = '))
b = int(input('Ievadiet skaitli = '))
darbiba = input('+, -, *, /:')

if darbiba == '+':
    c = a+b
elif darbiba == '-':
    c = a-b
elif darbiba == '*':
    c = a*b
elif darbiba == '/':
    c = a/b
else: 
    c = 'Mistake, try again'
print('Answer = ', c)