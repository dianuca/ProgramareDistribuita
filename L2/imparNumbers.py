while True:
    try:
        n = int(input("Introduceti un numar: "))
        break
    except:
        print("Va rog introduceti un numar valid!")
        continue
for i in range(1,n):
    if i%2 !=0 :
        print(i,end=' ') # end = sa se afiseze caracterele pe aceeasi linie