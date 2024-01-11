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