telefons = {
'Jānis':23543523,
'Rita': 23231244,
'Anna': 24567813
}

#Jānim ir 2 tel numuri 
telefons.update({'Jānis': 2324242})
print("Šis ir Ritas nr",telefons['Rita'])
print("Šis ir Jāņa nr",telefons['Jānis'])
print("Šis ir Annas nr",telefons['Anna'])

#Izveidot vārdnīcu ar atslēgu virkni un fromkeys() metodi
#Vārdnīca nenorādot ierakstu vērtības

kk = ('Viens', "Divi", "Trīs") 
dd = dict.fromkeys(kk) #Izprintē none, jo nav vērtības norādītas
print(dd)
val = 0 #Šī vērtība būs visai vārdnīcai
dd = dict.fromkeys(kk,val)
print(dd)

#Izveidot vārdnīcu, kas satur sarakstu
valstis ={
    "Latvija": ['Liepāja', "Rīga", "Bauska"],
    "Somija": ['Helsinki', 'Tampere', 'Rovaniemi'],
    "Igaunija": ['Pērnava', 'Tallina', 'Rakvere']
}

for atslega, vertiba in valstis.items():
    for i in vertiba:
        print("{}:{}".format(atslega,i))
    print("* * * * * * * * *")