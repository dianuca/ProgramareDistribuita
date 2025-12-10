def convert_temperature(g : float, t1 : str, t2 : str) -> float:
    if t1 == 'c':
        if t2 == 'f':
            return g*9/5+32
        else:
            return g + 273.15
    elif t1 == 'f':
        if t2 == 'c':
            return (g-32)*5/9
        else:
            return (g-32)*5/9 + 273.15
    else:
        if t2 == 'c':
            return g-273.15
        else:
            return (g-273.15)*9/5+32

#pt citire le vom lua pe rand tocmai pentru a putea reintroduce datele unde am ramas

#pentru grade
while True:
    try:
        g = float(input("Grade: "))
        break
    except ValueError as e:
        print("A aparut o eroare:", e)
        continue

#pentru t1
while True:
    try:
        t1 = input("T1 (C, F sau K): ")
        if (len(t1) != 1):
            raise ValueError("Introduceti un singur caracter pentru T1.")
        if (t1.lower() not in ['c', 'f', 'k']):
            raise ValueError("T1 trebuie sa fie doar C, F sau K")
        break
    except ValueError as e:
        print("A aparut o eroare:", e)

#pentru t2
while True:
    try:
        t2 = input("T2 (C, F sau K): ")
        if (len(t2) != 1):
            raise ValueError("Introduceti un singur caracter pentru T2.")
        if (t2.lower() not in ['c', 'f', 'k']):
            raise ValueError("T2 trebuie sa fie doar C, F sau K")
        break
    except ValueError as e:
        print("A aparut o eroare:", e)

t1 = t1.lower()
t2 = t2.lower()
print(convert_temperature(g, t1, t2))