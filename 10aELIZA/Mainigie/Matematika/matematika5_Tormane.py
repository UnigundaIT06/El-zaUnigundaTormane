import math

print("Programmu izstrādāja: Elīza Unigunda Tormane.  " )
print()
print("Laukuma aprēķins ģeometriskām figūrām")
print("\t***")
print("Ievadiet malas A garumu: ") 
malaA =float(input()) 
print(f'Malas A garums: ' "{:.1f}".format(malaA)) #Malas A garums tiek noapaļots ar vienu skaitli pēc komata
print("\t***")
print("Ievadiet malas B garumu: ")
malaB =float(input())
print(f'Malas B garums: ' "{:.1f}".format(malaB)) #Malas B garums tiek noapaļots ar vienu skaitli pēc komata
print("\t***")
print("Ievadiet augstumu: ") 
malas_augstums =float(input())
print(f'Augstums: ' "{:.1f}".format(malas_augstums))

print(f'Laukums trijstūrim: {malaA*malas_augstums/2}')  #Tiek ievadīta formula, kas aprēķina trijstūra laukumu 
print(f'Laukums trapecei: {(malaA+malaB)/2*malas_augstums}') #Tiek ievadīta formula, kas aprēķina trapecei laukumu
print(f'Laukums paralelogramam: {"{:.1f}".format(malaA*malas_augstums)}') #Tiek ievadīta formula, kas aprēķina paralelograma laukumu
print("\t***")
print("Paldies!")


