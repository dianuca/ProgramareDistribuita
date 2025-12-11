while True:
    try:
        a = input("Introduceti numar: ")
        a = int(a)
        break
    except:
        print("Input invalid, va rog introduceti din nou")

if a%2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")
