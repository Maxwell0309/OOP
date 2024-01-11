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