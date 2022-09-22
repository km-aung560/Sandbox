MIN_LENGTH = 10

password = input("Enter password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long.")
    password = input("Enter password: ")
print("*" * len(password))
