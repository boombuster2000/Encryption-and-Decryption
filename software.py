from cryptography.fernet import Fernet
from os import system

def display_menu():
    system("cls")
    print("1) Generate Key\n2) Encrypt Message\n3) Decrypt Message\n4) Settings\n5) Quit")
    print("----")

def get_settings():
    settings_UI = []
    with open("settings.txt","r") as f:
        txt_settings = f.readlines()

    settings_UI.append(txt_settings[0])
    settings_UI[0] = settings_UI[0].strip()

    txt_settings[1] = txt_settings[1].lower()
    if txt_settings[1] == "true":
        settings_UI.append("✅")
    elif txt_settings[1] == "false":
        settings_UI.append("❌")
    else:
        print("else")
        with open("settings.txt", "w") as f:
            f.write(txt_settings[0] + "\n")
            f.write(txt_settings[1])
        settings_UI.append("✅")
        
    return settings_UI

def display_settings():
    system("cls")

    print("1) Default Key: " + settings_UI[0] + "\n2) Save key to file automatically: "+ settings_UI[1] +" \n3) Main Menu")
    print("----")  

def change_settings(settings_option):
    default_key,save_key = get_settings()
    settings_UI = [default_key,"✅"]

    if settings_option == "1": # change default key
        system("cls")
        default_key = input("Enter key: ")
        settings_UI[0] = default_key
        with open("settings.txt","w") as f:
            f.writelines([default_key,save_key])

        display_settings()

    elif settings_option == "2":
        if settings_UI[1] == "❌":
            settings_UI[1] = "✅"
            with open("settings.txt","w") as f:
                f.writelines([default_key, "True"])

        elif settings_UI[1] == "✅":
            settings_UI[1] = "❌"
            with open("settings.txt", "w") as f:
                f.writelines([default_key, "False"])

        display_settings()

def generate_key():
    with open("key.txt","w") as f:
        key = Fernet.generate_key()
        f.write(str(key,"utf8"))
    print("Key is: " + str(key,"utf8")+ "\n")
    print("!!!ANYONE WITH KEY CAN DECRYPT YOUR MESSAGES!!!")
    print("Store this somewhere safe, by default a txt file is made/overwritten.")
    system("pause")
    system("cls")

def encryption():
    try:
        encrypted_message = crypter.encrypt(bytes(input("Enter message: "),"utf-8"))
        print("Encrypted message is: "+ str(encrypted_message,"utf8"))
    except:
        print("Can't encrypt message.")
    system("pause")

def decryption():
    try:
        decrypted_message = crypter.decrypt(bytes(input("Enter  encrypted message: "),"utf-8"))
        print("Decrypted message is: "+ str(decrypted_message,"utf8"))
    except:
        print("Can't decrypt.")
    system("pause")

system("cls")

default_key,save_key = get_settings()
settings_UI = get_settings()

while True:

    while True: # selecting option
        display_menu()
        menu_option = input("")
        if menu_option == "1" or menu_option == "2" or menu_option == "3" or menu_option == "4" or menu_option == "5":
            display_menu()
            break

    if menu_option == "1": # generate key
        generate_key()

    elif menu_option == "2": # encryption
        if settings_UI[0] == "" or settings_UI[0] == " ":
            try:
                key = bytes(input("Enter key: "),"utf-8")
                crypter = Fernet(key) # creates Fernet object, an algorithm with the key to decrypt and encrypt
            except:
                print("Invalid Key")
        else:
            key = bytes(default_key,"utf8")
        encryption()

    elif menu_option == "3": # decryption
        if settings_UI[0] == "" or settings_UI[0] == " ":
            try:
                key = bytes(input("Enter key: "),"utf-8")
                crypter = Fernet(key) # creates Fernet object, an algorithm with the key to decrypt and encrypt
            except:
                print("Invalid Key")
        else:
            key = bytes(default_key,"utf8")
        decryption()

    elif menu_option == "4": # settings
        while True:
            while True:
                display_settings()
                settings_option = input("")
                if settings_option == "1" or settings_option == "2" or settings_option == "3":
                    break
            if settings_option == "1" or settings_option == "2":
                change_settings(settings_option)
            elif settings_option == "3":
                break

    elif menu_option == "5": # quit
        break