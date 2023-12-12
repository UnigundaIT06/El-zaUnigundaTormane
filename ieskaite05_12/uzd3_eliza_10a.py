skaitli =[] #Tukšais saraksts


skaitlu_skaits = int(input("Skaitļu skaits sarakstā (ne mazāk kā 3): "))
if skaitlu_skaits <3:
        print("Skaitļu skaits ir mazāks par trīs! Ievadiet vēlreiz.")
        while skaitlu_skaits <3: #Kamēr ievadītais skaitļu skaits ir mazāk par trīs, tikmēr lūgs lietotājam ievadīt atkal
            skaitlu_skaits = int(input("Skaitļu skaits sarakstā (ne mazāk kā 3): "))
if skaitlu_skaits >=3:
                 
 
 
                for i in range (skaitlu_skaits):
                    skaitlis = int(input("Ievadiet skaitli: "))
                    skaitli.append(skaitlis) #Ievadītais skaitlis tiek pievienots sarakstam
                    print(skaitli)
                print("*****")
                print ("Lielākais skaitlis sarakstā ir: ", max(skaitli)) #Parāda lielāko skaitli no saraksta
        