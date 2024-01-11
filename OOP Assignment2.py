def main_menu():

    while True:
        print("HOME PAGE")
        print("1. COMPONENTS") 
        print("2. CIRCUIT KITS")
        print("3. CLOSE")
        choice = input("Please enter a number: ")

        if choice == '1':
            components_menu()
        elif choice == '2':
            circuit_kits_menu() 
        elif choice == '3':
            print("Closing program")
            break
        else:
            print("Wrong input, must be a number between 1 and 3 ")

def circuit_kits_menu():
    while True:
        print("CIRCUIT KIT MENU")
        print("1. NEW CIRCUIT KIT")
        print("2. VIEW CIRCUIT KITS")
        print("3. BACK")
        choice = input("Please enter a number: ")

        if choice == '1':
            new_circuit_kit_menu()
            pass
        elif choice == '2':
            view_circuit_kits()
            pass
        elif choice == '3':
            break
        else:
            print("Wrong input, must be a number between 1 and 3")