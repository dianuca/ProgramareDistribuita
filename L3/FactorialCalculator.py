def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    try:
        n = int(input("Numarul n: "))
        break
    except:
        print("Introduceti o valoare corecta!")
        continue

print(factorial(n))