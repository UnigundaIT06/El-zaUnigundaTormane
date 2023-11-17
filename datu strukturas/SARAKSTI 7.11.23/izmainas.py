saraksts = [1,2,3,4,5,6,7,8,9]
saraksts.append('Cepums') #Pievieno beigās
print(saraksts)

#Izmet no beigām
saraksts.pop()
print(saraksts)

saraksts.insert(3, 'Hello!') #Ievieto trešo no kreisās
print(saraksts)

saraksts.remove(7) #Izdzēš norādīto vērtību
print(saraksts)

#funkcijas del pielietojums
tests = [1,2,3,4,5,6,7,8]
del tests[2] #Izdzēš vienu elementu
print(tests)

del tests[3:6]
print(tests)#Izdzēš intervālu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2] #no 2-7 elementam dzēš ārā katru otro
print(cipari)