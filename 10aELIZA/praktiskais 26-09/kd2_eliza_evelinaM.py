pirmSk = int(input('Ievadi pirmo skaitli: ')) #Lietotājs ievada pirmo un otro skaitli
otrSk = int(input('Ievadi otro skaitli: '))

summa = pirmSk+otrSk #Tiek izdarītas darbības: summa, gadījumam ja pirmais skaitlis ir 3, un starpība, gadījumā ja pirmais skaitlis nav 3
starpiba = pirmSk-otrSk

if pirmSk == 3: #Tiek noteikti vajadzīgie rezultāti
    print('Pirmais skaitlis ir 3, saskaitot abus skaitļus rezultāts ir: ',summa) 
elif pirmSk < 3 or pirmSk > 3:
    print('Pirmais skaitlis nav 3, atņemot otro skaitli no pirmā rezultāts ir: ',starpiba)
