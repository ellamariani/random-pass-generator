import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        print("Random Password:", password)
        run_again = input("Do you want to generate another password? (yes/no): ").lower()
        if run_again != 'yes':
            break

if __name__ == "__main__":
    main()
