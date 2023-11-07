#Vajadzīgās lietas, kas jāievada lietotājam!
username = "sniegavirs"
password = "20231"


username_in = input("Lūdzu, ievadiet savu lietotājvārdu: ")
if username_in == username:
         ()
else:
     again1 = username_in = input("Ir atlikuši vēl 4 mēģinājumi \nLūdzu, ievadiet savu lietotājvārdu:") * 1 #Izdevās, ka izvada tikai 1 reizi :(
     print(again1)

password_in = input("Lūdzu, ievadiet savu paroli: ") 
if len(password_in) < 5 : #Norāda, ka ja parolē būs mazāk par piecām rakstzīmēm - prasīs ievadīt atkal!
          print("Parolei jābūt 5 rakstzīmes garai!")
          again = password_in = input("Atlikuši vēl 4 mēģinājumi \nLūdzu, ievadiet savu paroli: ") * 1 #Izdevās, ka izvada tikai 1 reizi
          print(again)
elif password_in == password:
         print("Pieslēgšanās veiksmīga!")

#Lietotājs ievada input lauciņos veselos skaitļus
in1 = int(input("Ievadiet 1. veselo skaitli: "))
in2 = int(input('Ievadiet 2. veselo skaitli: '))
summa = sum(range(in1+1,in2)) #Tiek saskaitīti skaitļi, kas ir pa vidu. piem. 2 un 5 starpvidu skaitļu summa būs 7
print("Šo starp skaitļu summa ->", summa) #Izvada summu
       

if in1 > in2: #Tiek veiktas if funkcijas, kuras strādā atbilstošā gadījumā
        print("Rezultāts 0, jo pirmais skaitlis ir lielāks par otro")
elif in2 == "stop":
        print("Programma beigusies!")
        exit() #Beidz programmu
elif in1 == "stop":
         print("Programma beigusies!")
         exit() #Beidz programmu
elif in1 < 0 or in2 < 0:
        print("Nedrīkst būt negatīvs skaitlis!") #Kaut vai uzrāda, ka nedrīkst (summa vēl projām izprintējas)



        





