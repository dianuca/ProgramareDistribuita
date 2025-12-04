while True:
    try:
        c = input ("Introduceti tmp in grade Celsius: ")
        c = float(c)
        break
    except:
        print("Input invalid! Va rog introduceti un numar.")
f = c*9/5+32
print("Grade Fahrenheit: ", f)