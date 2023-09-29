pirmSk = int(input('Ievadi pirmo skaitli: ')) #Lietotājs ievada pirmo un otro skaitli
otrSk = int(input('Ievadi otro skaitli: '))

if pirmSk and otrSk > 10 and pirmSk and otrSk < 25:
    print('Tev izdevās izpildīt uzdevumu!')
elif pirmSk or otrSk > 10 and pirmSk or otrSk < 25:
    print('Jāpielabo uzdevuma izpilde!')
else:
    print('Neizdevās izpildīt!')
