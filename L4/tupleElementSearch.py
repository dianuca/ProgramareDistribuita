def cautare(tupla: tuple, valoare: int):
    if valoare in tupla:
        index = tupla.index(valoare) #salvam indexul daca gasim valoarea
        print(valoare,"se gaseste in tupla la indexul", index)
    else:
        print("valoare",valoare,"nu se gaseste in tupla")

#tupla - esta ca un vector ordonat, care nu poate fi modidicata dupa creare
while True:
    try:
        v = input("Introdu valorile: ")
        lista = v.split(",")
        tupla = tuple(map(int,lista)) #map: aplica functia int pe fiecare element
        break
    except:
        print("Eroare!")
        continue

while True:
    try:
        v = input("Introdu valoarea cautata: ")
        v = int(v)
        break
    except:
        print("Eroare!")
        continue

cautare(tupla, v)