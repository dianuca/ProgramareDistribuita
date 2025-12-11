import random

x = random.randint(1,20) #pentru generarea unui numar random intre doua valori
gasit = False
for i in range (0,5):
    try:
        g = int(input(f"Incercarea {i+1}: "))
    except:
        print("Va rog introduceti un numar",i+1)
        continue #pentru a lasa utilizatorul sa mai introduca date
    if g < x :
        print("Numarul",g,"este prea mic!")
    elif g >x :
        print("Numarul",g,"este prea mare!")
    else:
        print("Ati ghicit numarul!")
        gasit = True
        break
if gasit == False:
    print ("Nu ati ghicit numarul. Numarul era",x);