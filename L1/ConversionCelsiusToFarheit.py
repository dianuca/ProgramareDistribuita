try:
    c = input ("Introduceti temp in grade Celsius: ")
    c = float(c)
    f = c*9/5+32
    print("Grade Farnheit ",f)
except:
    print("Eroare: introduceti un numar valid")