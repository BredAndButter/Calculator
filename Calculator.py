import time

while True:

    print("")
    a = input("Choose operation: ")

    if a == "+":
        print("")
        b = input("Input first number: ")
        b = float(b)
        print("")
        c = input("Input second number: ")
        c = float(c)
        print("")
        print(b + c)
        time.sleep(0.5)

    elif a == "-":
        print("")
        b = input("Input first number: ")
        b = int(b)
        print("")
        c = input("Input second number: ")
        c = float(c)
        print("")
        print(b - c)
        time.sleep(0.5)

    elif a == "*":
        print("")
        b = input("Input first number: ")
        b = float(b)
        print("")
        c = input("Input second number: ")
        c = float(c)
        print("")
        print(b * c)
        time.sleep(0.5)

    elif a == "/":
        print("")
        b = input("Input first number: ")
        b = float(b)
        print("")
        c = input("Input second number: ")
        c = float(c)
        print("")
        print(b / c)
        time.sleep(0.5)

    elif a == "q":
        print("")
        time.sleep(3)
        break

    else:
        print("")
        print("Did not understand user input.")
        time.sleep(0.5)
