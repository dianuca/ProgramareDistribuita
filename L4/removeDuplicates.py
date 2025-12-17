while True:
    try:
        x = input("Introdu valorile: ")
        lista = x.split(",")
        tupla = tuple(map(int,lista))
        break
    except:
        print("Valori invalide")
        continue

list_fin = []
#verificam daca exista valoarea in vectorul de il creem
for x in range(0,len(tupla)) :
    if tupla[x] in list_fin:
        continue
    else:
        list_fin.append(tupla[x])
print(list_fin)
