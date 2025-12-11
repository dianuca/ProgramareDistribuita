while True:
    try:
        p = input ("Introduceti principalul: ")
        p = float(p)
        r = input ("Introduceti rata anuala: ")
        r = float(r)
        t = input ("Introduceti timpul in ani: ")
        t = int(t)
        break
    except:
        print("Va rog introduceti un numar valid.")
interest = (p*r*t) / 100
print("Interesul este: ",interest)