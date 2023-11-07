'''>Izveidot 3 sarakstus:lietotajs pats norādīs cik elementus likt sarakstā
>Pirmā un otrā saraksta vērtības - ievada lietotājs
>Trešā saraksta vērtības iegūst apvienojot pirmos 2 sarakstus.
>Katra saraksta saturu - glīti parādīt uz ekrāna.
'''
saraksts1 = []
saraksts2 = []
saraksts3 = []



el1 = int(input(print("Garums")))
for i in range(0,el1):
    ele = int(input("Ievadiet elementus:"))
    saraksts1.append(ele)  
    print(saraksts1)

el2 = int(input(print("Garums")))
for i in range(0,el2):
    ele2 = input("Ievadiet elementus:")
    saraksts2.append(ele2)  
    print(saraksts2)

print("_________________________")
saraksts3 = saraksts1 + saraksts2
print(saraksts3)





list1 = []
list2 = []
#pirmais saraksts
print("Ievadi saraksta garumu: ")
garums = int(input()) #Lietotājs pats ievada sarakstu
for i in range(garums):
    lieta1 = input("Ievadiet saraksta elementu:")
    list1.append(lieta1)
    print("Pirmā saraksta elementi", list1)

print("Ievadi saraksta garumu: ")
garums2 = int(input()) #Lietotājs pats ievada sarakstu
for i in range(garums2):
    lieta2 = input("Ievadiet saraksta elementu:")
    list2.append(lieta2)
    print("Pirmā saraksta elementi", list2)


