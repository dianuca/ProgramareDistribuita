while True:
    try:
        x = input("Introduceti numerele, separate prin virgula: ")
        list = x.split(",") #un vector de tip string
        lista_numere = [] #un vector de tip int unde stocam
        for x in list :
            lista_numere.append(int(x)) #adaugam convertit
        break
    except:
        print("Eroare")
        continue
print("Maximul este:", max(lista_numere))
print("Minimum este:", min(lista_numere))
