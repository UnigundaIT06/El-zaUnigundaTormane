saraksts_skaitļi = [1, 2, 7, 8, 5, 3, 5, 5, 2, 2] 
print("Saraksts: ",saraksts_skaitļi)
print("*****")
para_skaitli = 0 #pāra un nepāra skaitļi tiek definēti, kā nulle sākumā
nepara_skaitli = 0 

for summa in saraksts_skaitļi: #Tiek apskatīts katrs skaitlis sarakstā
    if summa % 2 == 0: #Ja skaitli var izdalīt ar divi, tad tas ir pāra
        para_skaitli += 1 #Pie definētajiem 0 skaitļiem, tiek pieskaitīts katrs skaitlis, kas atbilst prasībām
    else: #Ja skaitli nevar izdalīt
        nepara_skaitli +=1  

print("Pāra skaitļu skaits: ", para_skaitli)
print("Nepāra skaitļu skaits: ", nepara_skaitli)