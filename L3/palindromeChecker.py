def _palindrome(word : str) -> bool: #o functie care are un param string si returneaza o val bool
    i = 0;
    j = len(word)-1;
    gasit = True
    while i < j and gasit == True:
        if word[i] != word[j]:
            gasit = False
        else:
            i += 1
            j -= 1
    if gasit == True:
        return True
    else:
        return False

while True:
    try:
        word = str(input("Introducet sir: "))
        break
    except:
        print("Introduceti un sir valid!")
        continue

if _palindrome(word) == True:
    print("Cuvantul",word,"este palindrom")
else:
    print("Cuvantul",word,"nu este palindrom")