'''atbilde = 'j'
while atbilde == "j":
    print("Nekusties! ")
    atbilde = input("Vai briesmonis ir draudzīgs? (j/n)")
print('Bēdz prom!')'''

#Pārbaudīt vai lietotājs prot reizināt ar 7
# programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautajumi


r = int(input("Reizinātājs >"))
for i in range(1,13): 
    print("Cik ir",i,"x",r,'?')
    minejums = input()
    if minejums == 'stop':
        break 
    if minejums == 'izlaist':
        print("Tiek izlaists 1 jautājums")
        continue #izlaiž 1 jautājumu un turpina tālāk
    atbilde = i * r
    if int(minejums) == atbilde:
        print('Pareizi!')
    else: 
        print('Nepareizi, tas ir',atbilde) 
     #ja ir nepareizi, tad atgriežas pie jautājuma
     #reizinātāju ievada lietotājs