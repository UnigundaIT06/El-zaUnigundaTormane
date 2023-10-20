#Izdrukāt skaitļus 0,1,2,3,4,5
for i in range(6):#defaultā sāksies ar 0 
    print(i)
print('* * * ')
#Izdrukāt 3,5,7
for i in range(3,8,2):
    print(i)
print("* * *")

n = int(input("Ievadīt skaitli:"))
for i in range(1,11):
    print(n,'+',i,'=',n+i)
print("* * *")
#Atrast skaitļu 2 un 4 dalītājus
# uz ekrāna parādīt tos, kas dalās ar 2, tos, dalās gan ar 4, gan ar 2
#range 50

s = int(input("Ievadat diapozonu > " ))
for i in range(51): 
    if i%2==0 and i%4==0:
        print(i,":dalas ar 2 un ar 4")
    elif i%2==0:
        print(i,":dalas ar 2")
    else:
        print(i)