try:
    print("Welcome")

    integer = int(input("Enter any number: "))

    for i in range(1, 13):
        print(f"{integer} x {i} = {integer * i}")

except:
    print("invalid input, numbers only (e.g. 5)")