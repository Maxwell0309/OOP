def get_user_input(prompt, valid_choices):
    while True:
        user_input = input(prompt)
        if user_input in valid_choices:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {valid_choices}")

def select_component(components):
    for i, component in enumerate(components, 1):
        print(f"{i}. {component}")
    choice = get_user_input("Please select an index: ", [str(i) for i in range(1, len(components) + 1)])
    quantity = input(f"Please enter number of {components[int(choice) - 1]}: ")
    return components[int(choice) - 1], quantity

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


def new_circuit_kit_menu():
    while True:
        print("NEW CIRCUIT KIT MENU")
        print("1. LIGHT GLOBE CIRCUIT KIT")
        print("2. LED LIGHT CIRCUIT KIT")
        print("3. SENSOR CIRCUIT KIT WITH LIGHT GLOBE")
        print("4. SENSOR CIRCUIT KIT WITH LED LIGHT")
        print("5. SENSOR CIRCUIT KIT WITH BUZZER")
        print("6. SENSOR CIRCUIT KIT WITH LIGHT GLOBE AND SWITCH")
        print("7. SENSOR CIRCUIT KIT WITH LED LIGHT AND SWITCH")
        print("8. SENSOR CIRCUIT KIT WITH BUZZER AND SWITCH")
        print("9. BACK")
        choice = input("Please enter a number: ")

        if choice == '1':
            create_light_globe_circuit_kit()
        elif choice == '2':
            create_led_light_circuit_kit()
        elif choice == '3':
            create_sensor_circuit_kit_with_light_globe()
        elif choice == '4':
            create_sensor_circuit_kit_with_led_light()
        elif choice == '5':
            create_sensor_circuit_kit_with_buzzer()
        elif choice == '6':
            create_sensor_circuit_kit_with_light_globe_and_switch()
        elif choice == '7':
            create_sensor_circuit_kit_with_led_light_and_switch()
        elif choice == '8':
            create_sensor_circuit_kit_with_buzzer_and_switch()
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
    selected_globe, globe_quantity = select_component(light_globes)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating Light Globe Circuit Kit with:")
    print(selected_globe, "x", globe_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)

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
    selected_led, led_quantity = select_component(led_lights)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating LED Light Circuit Kit with:")
    print(selected_led, "x", led_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)

def create_sensor_circuit_kit_with_light_globe():
    print("SENSOR CIRCUIT KIT WITH LIGHT GLOBE")

    sensors = [
        "5.0V Motion Sensor $3.90 x 6",
        "6.0V Infrared Sensor $4.70 x 4",
        "5.0V Dust Sensor $3.90 x 1"
    ]
    selected_sensor, sensor_quantity = select_component(sensors)

    light_globes = [
        "6.5V 240.0mA Warm Light Globe $3.50 x 11",
        "7.2V 240.0mA Neutral Light Globe $3.60 x 8",
        "7.6V 280.0mA Cool Light Globe $3.70 x 6",
        "6.5V 240.0mA Cool Light Globe $3.50 x 4"
    ]
    selected_globe, globe_quantity = select_component(light_globes)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating Sensor Circuit Kit with Light Globe:")
    print(selected_sensor, "x", sensor_quantity)
    print(selected_globe, "x", globe_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)

def create_sensor_circuit_kit_with_led_light():
    print("SENSOR CIRCUIT KIT WITH LED LIGHT")

    sensors = [
        "5.0V Motion Sensor $3.90 x 6",
        "6.0V Infrared Sensor $4.70 x 4",
        "5.0V Dust Sensor $3.90 x 1"
    ]
    selected_sensor, sensor_quantity = select_component(sensors)

    led_lights = [
        "3.0V 150.0mA Red LED Light $2.20 x 20",
        "3.0V 150.0mA Green LED Light $2.20 x 15",
        "4.0V 180.0mA White LED Light $2.20 x 18",
        "3.2V 240.0mA Aqua LED Light $4.80 x 4",
        "6.5V 280.0mA Green LED Light $3.50 x 4",
        "6.5V 240.0mA Red LED Light $3.50 x 5"
    ]
    selected_led, led_quantity = select_component(led_lights)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating Sensor Circuit Kit with LED Light:")
    print(selected_sensor, "x", sensor_quantity)
    print(selected_led, "x", led_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)


def create_sensor_circuit_kit_with_buzzer():
    print("SENSOR CIRCUIT KIT WITH BUZZER")

    sensors = [
        "5.0V Motion Sensor $3.90 x 6",
        "6.0V Infrared Sensor $4.70 x 4",
        "5.0V Dust Sensor $3.90 x 1"
    ]
    selected_sensor, sensor_quantity = select_component(sensors)

    buzzers = [
        "4.0V 120.0mA 240.0Hz 90dB Buzzer $5.60 x 6",
        "3.2V 140.0mA 140.0Hz 80dB Buzzer $4.40 x 6"
    ]
    selected_buzzer, buzzer_quantity = select_component(buzzers)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating Sensor Circuit Kit with Buzzer:")
    print(selected_sensor, "x", sensor_quantity)
    print(selected_buzzer, "x", buzzer_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)

def create_sensor_circuit_kit_with_light_globe_and_switch():
    print("SENSOR CIRCUIT KIT WITH LIGHT GLOBE AND SWITCH")

    sensors = [
        "5.0V Motion Sensor $3.90 x 6",
        "6.0V Infrared Sensor $4.70 x 4",
        "5.0V Dust Sensor $3.90 x 1"
    ]
    selected_sensor, sensor_quantity = select_component(sensors)

    light_globes = [
        "6.5V 240.0mA Warm Light Globe $3.50 x 11",
        "7.2V 240.0mA Neutral Light Globe $3.60 x 8",
        "7.6V 280.0mA Cool Light Globe $3.70 x 6",
        "6.5V 240.0mA Cool Light Globe $3.50 x 4"
    ]
    selected_globe, globe_quantity = select_component(light_globes)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating Sensor Circuit Kit with Light Globe and Switch:")
    print(selected_sensor, "x", sensor_quantity)
    print(selected_globe, "x", globe_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)

def create_sensor_circuit_kit_with_led_light_and_switch():
    print("SENSOR CIRCUIT KIT WITH LED LIGHT AND SWITCH")

    sensors = [
        "5.0V Motion Sensor $3.90 x 6",
        "6.0V Infrared Sensor $4.70 x 4",
        "5.0V Dust Sensor $3.90 x 1"
    ]
    selected_sensor, sensor_quantity = select_component(sensors)

    led_lights = [
        "3.0V 150.0mA Red LED Light $2.20 x 20",
        "3.0V 150.0mA Green LED Light $2.20 x 15",
        "4.0V 180.0mA White LED Light $2.20 x 18",
        "3.2V 240.0mA Aqua LED Light $4.80 x 4",
        "6.5V 280.0mA Green LED Light $3.50 x 4",
        "6.5V 240.0mA Red LED Light $3.50 x 5"
    ]
    selected_led, led_quantity = select_component(led_lights)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating Sensor Circuit Kit with LED Light and Switch:")
    print(selected_sensor, "x", sensor_quantity)
    print(selected_led, "x", led_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)


def create_sensor_circuit_kit_with_buzzer_and_switch():
    print("SENSOR CIRCUIT KIT WITH BUZZER AND SWITCH")

    sensors = [
        "5.0V Motion Sensor $3.90 x 6",
        "6.0V Infrared Sensor $4.70 x 4",
        "5.0V Dust Sensor $3.90 x 1"
    ]
    selected_sensor, sensor_quantity = select_component(sensors)

    buzzers = [
        "4.0V 120.0mA 240.0Hz 90dB Buzzer $5.60 x 6",
        "3.2V 140.0mA 140.0Hz 80dB Buzzer $4.40 x 6"
    ]
    selected_buzzer, buzzer_quantity = select_component(buzzers)

    switches = [
        "4.5V Push Switch $4.60 x 12",
        "4.5V Toggle Switch $4.80 x 1"
    ]
    selected_switch, switch_quantity = select_component(switches)

    batteries = [
        "1.2V AA Battery $2.60 x 12",
        "1.5V AAA Battery $2.70 x 8",
        "1.5V AA Battery $3.10 x 15",
        "1.5V AAA Battery $3.10 x 1"
    ]
    selected_battery, battery_quantity = select_component(batteries)

    wires = [
        "40mm Wire $2.40 x 24",
        "60mm Wire $3.20 x 56",
        "80mm Wire $4.60 x 25"
    ]
    selected_wire, wire_quantity = select_component(wires)

    print("Creating Sensor Circuit Kit with Buzzer and Switch:")
    print(selected_sensor, "x", sensor_quantity)
    print(selected_buzzer, "x", buzzer_quantity)
    print(selected_switch, "x", switch_quantity)
    print(selected_battery, "x", battery_quantity)
    print(selected_wire, "x", wire_quantity)