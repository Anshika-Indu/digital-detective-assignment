number = int(input("Enter a positive decimal number: "))

if number <= 0:
    print("Please enter a positive whole number.")
else:
    print("Binary:", bin(number)[2:])
    print("Hexadecimal:", hex(number)[2:].upper())
