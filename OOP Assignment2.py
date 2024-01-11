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


def create_light_globe_circuit_kit():

    print("LIGHT GLOBE CIRCUIT KIT")


    light_globes = [
        "6.5V 240.0mA Warm Light Globe $3.50 x 11",
        "7.2V 240.0mA Neutral Light Globe $3.60 x 8",
        "7.6V 280.0mA Cool Light Globe $3.70 x 6",
        "6.5V 240.0mA Cool Light Globe $3.50 x 4"
    ]
    for i, globe in enumerate(light_globes, 1):
        print(f"{i}. {globe}")
    globe_choice = input("Please select the light globe index: ")


    globe_quantity = input(f"Please enter number of {light_globes[int(globe_choice)-1]}: ")

    print("Select type of switch")
    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    for i, switch in enumerate(switches, 1):
        print(f"{i}. {switch}")
    switch_choice = input("Please select the switch index: ")

    switch_quantity = input(f"Please enter number of {switches[int(switch_choice)-1]}: ")

    print("Select type of battery")
    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    for i, battery in enumerate(batteries, 1):
        print(f"{i}. {battery}")
    battery_choice = input("Please select the battery index: ")

    battery_quantity = input(f"Please enter number of {batteries[int(battery_choice)-1]}: ")

    print("Select type of wire")
    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    for i, wire in enumerate(wires, 1):
        print(f"{i}. {wire}")
    wire_choice = input("Please select the wire index: ")

    wire_quantity = input(f"Please enter number of {wires[int(wire_choice)-1]}: ")

    print("Creating Light Globe Circuit Kit with:")
    print(light_globes[int(globe_choice)-1], "x", globe_quantity)
    print(switches[int(switch_choice)-1], "x", switch_quantity)
    print(batteries[int(battery_choice)-1], "x", battery_quantity)
    print(wires[int(wire_choice)-1], "x", wire_quantity)

def create_led_light_circuit_kit():
    print("LED LIGHT CIRCUIT KIT")

    led_lights = [
        "3.0V 150.0mA Red LED Light $2.20 x 20",
        "3.0V 150.0mA Green LED Light $2.20 x 15",
        "4.0V 180.0mA White LED Light $2.20 x 18",
        "3.2V 240.0mA Aqua LED Light $4.80 x 4",
        "6.5V 280.0mA Green LED Light $3.50 x 4",
        "6.5V 240.0mA Red LED Light $3.50 x 5"
    ]
    for i, led in enumerate(led_lights, 1):
        print(f"{i}. {led}")
    led_choice = input("Please select the LED light index: ")

    led_quantity = input(f"Please enter number of {led_lights[int(led_choice)-1]}: ")

    print("Select type of switch")
    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    for i, switch in enumerate(switches, 1):
        print(f"{i}. {switch}")
    switch_choice = input("Please select the switch index: ")

    switch_quantity = input(f"Please enter number of {switches[int(switch_choice)-1]}: ")

    print("Select type of battery")
    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    for i, battery in enumerate(batteries, 1):
        print(f"{i}. {battery}")
    battery_choice = input("Please select the battery index: ")

    battery_quantity = input(f"Please enter number of {batteries[int(battery_choice)-1]}: ")

    print("Select type of wire")
    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    for i, wire in enumerate(wires, 1):
        print(f"{i}. {wire}")
    wire_choice = input("Please select the wire index: ")

    wire_quantity = input(f"Please enter number of {wires[int(wire_choice)-1]}: ")

    print("Creating LED Light Circuit Kit with:")
    print(led_lights[int(led_choice)-1], "x", led_quantity)
    print(switches[int(switch_choice)-1], "x", switch_quantity)
    print(batteries[int(battery_choice)-1], "x", battery_quantity)
    print(wires[int(wire_choice)-1], "x", wire_quantity)