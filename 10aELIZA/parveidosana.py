#int pārveidošana par str
a = 5
b = 7
print('Skaitlis:', a + b)
print('Teksts:',str(a) + str(b)) #concat 

#izveidot 2 str tipa mainīgos(vērtība '123' un '456')
#pārveidot šos mainīgos par int tipu
#noteikt datu tipu

tekst1 = '123'
tekst2 = '456'
t1 = int(tekst1)
t2 = int(tekst2)
print(t1+t2, type(t2+t1))