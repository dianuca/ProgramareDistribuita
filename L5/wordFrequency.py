import string

def word_frequency(sir : str):
    sir = sir.lower()
    #parcurgem fiecare carcater din punctuatie si inlocuim aparitiile cu nimic
    for semn in string.punctuation:
        sir = sir.replace(semn,"")
    cuvinte = sir.split(" ")
    frecventa = {} #dictionar
    for c in cuvinte:
        if c in frecventa: #verificam daca cuvantul este in dictionar
            frecventa[c] += 1 #true: marim valoarea
        else:
            frecventa[c] = 1 #false: il adaugam in dictionar
    for cuvant, count in frecventa.items():
        print(f"{cuvant}: {count}",end=" ")

while True:
    try:
        v = input("Input text: ")
        break
    except:
        print("Introduceti alte valori!")

word_frequency(v)

