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

def view_circuit_kits():
    circuit_kits_list = [
        "8 PIECE SENSOR CIRCUIT WITH 1 X 1.8V 0.6MA SOLAR PANEL $16.00 1 X 5.0V MOTION SENSOR $3.90 1 X 4.0V 120.0MA 240.0HZ 90DB BUZZER $5.60 1 X 4.5V TOGGLE SWITCH $4.80 X 2",
        "6 PIECE SENSOR CIRCUIT WITH 1 X 1.5V AA BATTERY $3.10 1 X 5.0V DUST SENSOR $3.90 1 X 6.5V 240.0MA RED LED LIGHT $3.50 X 2",
        "16 PIECE LIGHT CIRCUIT WITH 1 X 1.5V AAA BATTERY $3.10 4 X 6.5V 240.0MA RED LED LIGHT $3.50 1 X 4.5V PUSH SWITCH $4.60 X 6",
        "16 PIECE LIGHT CIRCUIT WITH 1 X 1.5V AAA BATTERY $3.10 4 X 6.5V 280.0MA GREEN LED LIGHT $3.50 1 X 4.5V PUSH SWITCH $4.60 X 4",
        "21 PIECE LIGHT CIRCUIT WITH 2 X 1.5V AA BATTERY $3.10 4 X 6.5V 240.0MA COOL LIGHT GLOBE $3.50 1 X 4.5V ROCKER SWITCH $4.60 X 3",
        "21 PIECE LIGHT CIRCUIT WITH 2 X 1.5V AA BATTERY $3.10 4 X 6.5V 240.0MA WARM LIGHT GLOBE $3.50 1 X 4.5V PUSH SWITCH $4.60 X 3",
        "14 PIECE LIGHT CIRCUIT WITH 2 X 1.2V AA BATTERY $2.60 3 X 7.6V 280.0MA COOL LIGHT GLOBE $3.70 2 X 4.5V PUSH SWITCH $4.60 X 1"
    ]

    print("ALL CIRCUIT KITS")
    for i, kit in enumerate(circuit_kits_list, 1):
        print(f"{i}. {kit}")
    print(f"{len(circuit_kits_list) + 1}. BACK")

    while True:
        try:
            choice = int(input("Please enter a number: "))
            if 0 < choice <= len(circuit_kits_list):
                manage_circuit_kit(circuit_kits_list[choice - 1])
            elif choice == len(circuit_kits_list) + 1:
                return
            else:
                print("Number is out of range, please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def manage_circuit_kit(kit):
    print(kit)
    print("1. SELL")
    print("2. PACK")
    print("3. UNPACK")
    print("4. BACK")

    while True:
        select = input("Please enter a number in 1-4: ")
        if select == "1":
            print("Selling", kit)
            number = input("Please enter number of " + kit + ": ")
            print("Sold", kit, "X", number)
        elif select == "2":
            print("Packing", kit)
            number = input("Please enter number of " + kit + ": ")
            print("Packed", kit, "X", number)
        elif select == "3":
            print("Unpacking", kit)
            number = input("Please enter number of " + kit + ": ")
            print("Unpacked", kit, "X", number)
        elif select == "4":
            return
        else:
            print("Wrong select, please try again.")

def new_component_menu():
    while True:
        print("NEW COMPONENT MENU")
        print("1. WIRE")
        print("2. BATTERY")
        print("3. SOLAR PANEL")
        print("4. LIGHT GLOBE")
        print("5. LED LIGHT")
        print("6. SWITCH")
        print("7. SENSOR")
        print("8. BUZZER")
        print("9. BACK")
        choice = input("Please enter a number: ")

        if choice == '1':
            new_wire()
        elif choice == '2':
            new_battery()
        elif choice == '3':
            new_solar_panel()
        elif choice == '4':
            new_light_globe()
        elif choice == '5':
            new_led_light()
        elif choice == '6':
            new_switch()
        elif choice == '7':
            new_sensor()
        elif choice == '8':
            new_buzzer()
        elif choice == '9':
            break
        else:
            print("Wrong input, must be a number between 1 and 9")

