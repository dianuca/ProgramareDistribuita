while True:
    try:
        s = input("Introduceti scor procentual: ")
        s = int(s)
        break
    except:
        print("Eroare! Introduceti un scor procentual valid.")
if s >= 90 :
    print("Nota A")
elif s >= 80 :
    print("Nota B")
elif s>=70:
    print("Nota C")
elif s>=60:
    print("Nota D")
else:
    print("Nota E")

