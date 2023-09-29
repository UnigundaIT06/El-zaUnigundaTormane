import math 
import random
print("Ievadiet riņķa līnijas rādiusu:")
r=float(input()) #Decimāldaļas skaitlis
print(r)
print(f'Riņķa līnijas garums: {"{:.2f}".format(2*math.pi*r)} \nRiņķa līnijas laukums: {round(math.pi*r**2, 2)}') #Ievada formulas, kuras aprēķina vajadzīgos lielumus
print("Ievadiet taisnleņķa trijstūra pirmās katetes garumu: ")
k1=int(input()) 
print("Ievadiet taisnleņķa trijsūtra otrās katetes garumu: ")
k2=int(input())
print(f'Taisnleņķa trijstūra hipotenūzas garums: {round(math.sqrt(k1**2+k2**2), 2)}')
print(f'Gadījuma skaitlis no 0 -1:  {random.random()}') #Funkcija, kas nejauši ģenerēti skaitļi no 0-1