#Izveidot vārdnīcu ar datiem par automašīnu(4)

auto = {
    'Zīmols': 'Škoda',
    'Gads': 2001,
    'Krāsa': 'Tumši sarkans',
    'Riepas': "Ziemas"
}
dati = input("Ievadiet zīmolu, lai pārbaudītu: ")
if dati == auto["Zīmols"]:
    print("Ir vārdnīcā! 🚗")
elif dati == auto.values(): #?
    print("Auto ir kā vērtība! 🚗 ")
else:
    print("Šāda auto nav. 🚗")
