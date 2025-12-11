import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) #**2 inseamna la puterea 2

while True:
    try:
        x1 = int(input("x1= "))
        x2 = int(input("x2= "))
        y1 = int(input("y1= "))
        y2 = int(input("y2= "))
        break
    except:
        print("Introduceti numere valide!")
        continue

print("Distanta este: ", dist(x1, y1, x2, y2))

