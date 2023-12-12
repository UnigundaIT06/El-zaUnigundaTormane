#Izveidot vārdnīcu, kas satur sarakstu
valstis ={
    "Latvija": ['Liepāja', "Rīga", "Bauska", "Ventspils", "Dobele"],
    "Somija": ['Helsinki', 'Tampere', 'Rovaniemi', 'Oslo', "Kophagen"],
    "Igaunija": ['Pērnava', 'Tallina', 'Rakvere', 'Tallina', 'Pērnava'],
}

#Izdrukāt vārdnīcas elementus, piekļūstot vārdnīcā konkrētai atslēgai

for i in valstis["Somija"]:
    print(i)
    
for i in valstis["Latvija"]:
  
    print(i)
for i in valstis["Igaunija"]:
    print(i)

#Izprintēt pirmās 3 pilsētas Latvijā
print(valstis["Latvija"][:3])

#Printēt pēdējās 2 pilsētas no Somijas
print(valstis['Somija'][-2:])

#Izprintēt visas pilsētas no Igaunijas izņemot pēdējās 3
print(valstis["Igaunija"][:2])

#Iegūt otro un piekto pilsētu no Igaunijas
print(valstis["Igaunija"][1:6])