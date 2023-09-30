from cryptography.fernet import Fernet
from os import system

system("cls")
while True:
    option = input("1) Generate Key\n2) Encrypt\n3) Decrypt\n4) Quit\n----\n")
    try:
        if option == "1":
            key = Fernet.generate_key()
            print(str(key,"utf8"))
            system("pause")
        elif option == "2":
            key = bytes(input("Enter key: "),"utf-8")
            crypter = Fernet(key)
            message = crypter.encrypt(bytes(input("Enter message: "),"utf-8"))
            print(str(message, "utf8"))
            system("pause")

        elif option == "3":
            key = bytes(input("Enter key: "),"utf-8")
            crypter = Fernet(key)
            message = crypter.decrypt(bytes(input("Enter message: "), "utf-8"))
            print(str(message, "utf8"))
            system("pause")
        elif option == "4":
            system("cls")
            break
        system("cls")
    except:
        print("Error")