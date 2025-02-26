n = int(input("Enter a number:"))
if (n <= 1):
    print(f"{n} is not a prime number")
elif (n % 1 == 0 and n % 2 != 0):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
