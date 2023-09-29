pirmSk = int(input('Ievadi pirmo skaitli: ')) #Lietotājs ievada pirmo un otro skaitli
otrSk = int(input('Ievadi otro skaitli: '))

reizinajums = pirmSk*otrSk #Tiek izdarītas darbības: summa, gadījumam ja reizinājums ir pozitīvs
summa = pirmSk+otrSk

if reizinajums > 0:
    print('Ievadīto skaitļu reizinājums ir: Pozitīvs, rezultāts ir: ',summa) #Tiek parādīts, vai reizinājums ir pozitīvs vai negatīvs, un atbilstošā gadījumā summēts
elif reizinajums < 0: 
    print('Ievadīto skaitļu reizinājums ir: Negatīvs. Nepieciešami citi skaitļi. ')
