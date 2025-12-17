def unique_pair_sum(sir,val) :
    for x in range(0,len(sir)-1) :
        gasit = False
        for y in range(x+1,len(sir)) :
            if sir[x] + sir[y] == val and sir[x] <= sir[y] :
                tupla = (sir[x],sir[y]) #creem tupla
                gasit = True
        if gasit == True :
            print(f"({tupla[0]},{tupla[1]})",end=" ")

while True :
    try:
        sir = input("Introduceti valori separate prin virgula: ")
        lista = sir.split(",")
        list = []
        for x in lista: #x-primul cuvant, etc
            list.append(int(x))
        break
    except:
        print("Valori invalide! Eroare")
        continue

while True:
    try:
        v = input("Introduceti target: ")
        v = int(v)
        break
    except:
        print("Eroare!")
        continue

unique_pair_sum(list,v)
