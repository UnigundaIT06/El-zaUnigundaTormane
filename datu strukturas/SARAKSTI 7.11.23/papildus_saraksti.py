#Piemērs sarakstam ar dažādiem datu tipiem
mixed_list = ['Suns', 7.25, 8, True]
            #   0       1   2    3 
print(mixed_list[2])

#Apgriezt skaitļu sarakstu 
skaitli = [1,2,3,4,5,6,7,3,4, 7, 8, 9,7]
apgriezts = list(reversed(skaitli))
print(apgriezts)

#Filtrēt tikai pāra skaitļus
para_skaitli = [num for num in skaitli if num %2 ==0]
print(para_skaitli)

#Iegūst saraksta garumu
#garums = len(skaitli)
#print(garums)

videjais = sum(skaitli)/len(skaitli)
print(f"videjais skaitlis:{videjais}")

#Atrast lielāko un mazāko skaitli, parādīt uz ekrāno no saraksta skaitli\
lielakais = max(skaitli)
mazakais = min(skaitli)
print("Lielākais skaitlis:",lielakais,"\nMazākais skaitlis:",mazakais)

list_fruits = ['Apple', 'Banana', 'Grapes', "Orange", 'Kiwi']
#Atrast vardus, kas sākas ar konkrētu burtu
varda_sakums = [vards for vards in list_fruits if vards.startswith('A')]
print(f"Vārdi, kas sākas ar 'A':{varda_sakums}")