while True:
    c = input("Intoduceti un caracter: ")
    if len(c) != 1:
        print("Introduceti un singur caracter.")
        continue
    if not c.isalpha():
        print("Eroare: ati introdus o cifra/caracter special!")
        break