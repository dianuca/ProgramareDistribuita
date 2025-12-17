def inverted_index(documente:str):
    dictionar = {} #creem un dictionar
    for i in range(len(documente)) : #parcurgem documentele
        text = documente[i].lower() #ignoram majusculele
        cuvinte = text.split() #eliminam spatiile

        for c in cuvinte : #parcurgem cuvintele din documentul i
            if c not in dictionar : #daca nu este adaugat
                dictionar[c] = set() #adaugam cuvantul, nu permitem duplicarea
            dictionar[c].add(i) #adaugam indexul documentului
    for c in dictionar :
        document = dictionar[c]
        print(f"{c}: {len(document)}")

while True:
    try:
        s = input("Introduceti documente, separate prin virgula: ")
        s = s.split(",") #eliminam virgula
        break
    except:
        print("Eroare!")
        continue

inverted_index(s)