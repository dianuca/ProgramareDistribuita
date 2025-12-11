while True:
    try:
        p = input("Introduceti un numar intreg prim: ")
        p = int(p)
        break
    except:
        print("Va rog introduceti un numar valid")
#verificarea propriu-zisa
prim = False
if p == 2 :
    prim = True
if p == 1 :
    prim = False
if p%2 == 0 and p!=2:
    prim = False
d = 3
while d*d < p and prim == False:
    if p%d == 0:
        prim = True
    d+=2
if prim == True:
    print("Numarul",p,"este prim")
else:
    print("Numarul",p,"nu este prim")