while True:
    try:
        x = int(input("Introduceti x: "))
        y = int(input("Introduceti y: "))
        break
    except:
        print("Eroare!")
#afisam multiplii de x, mai mici decat y
gasit = False
i = 1
while gasit == False:
    if i*x < y:
        print(i*x," "); #afisam multiplu
        i = i +1
    else:
        gasit = True
