pirmSk = int(input('Ievadi pirmo skaitli: ')) #Lietotājs ievada pirmo un otro skaitli
otrSk = int(input('Ievadi otro skaitli: '))

minus = pirmSk-otrSk #Tiek izdarītas darbības: summa, gadījumam ja pirmais skaitlis mazāks, starpība, ja pirmais skaitlis lielāks
plus = pirmSk+otrSk

if pirmSk > otrSk:
    print('Pirmais skaitlis ir: ',pirmSk,', otrs skaitlis ir: ', otrSk,'. Pirmais skaitlis ir lielāks par otru, starpība: ',minus)
elif pirmSk < otrSk:
    print('Pirmais skaitlis ir: ',pirmSk,', otrs skaitlis ir: ', otrSk,'. Pirmais skaitlis ir mazāks par otru, summa: ',plus)   #Tiek parādīts, vai pirmais skaitlis lielāks vai mazāks, parādīta atbilstoša summa/starpība
