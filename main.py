import csv

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15

def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin: float) -> float:
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def km_to_miles(km: float) -> float:
    miles = km / 1.609344
    return miles

def miles_to_km(miles: float) -> float:
    km = miles * 1.609344
    return km

def kg_to_pounds(kg: float) -> float:
    pounds = kg * 2.20462
    return pounds

def pounds_to_kg(pounds: float) -> float:
    kg = pounds / 2.20462
    return kg

def display_conversion_history(conversion_history: list) -> None:
    if not conversion_history :
        print("the conversion history is empty")
        return
    for index, item in enumerate(conversion_history, start=1):
        print(f'{index}. {item[0]} {float(item[1]):.2f} '
              f'= {item[2]} {float(item[3]):.2f}')

def load_conversion_history() -> list:
    conversion_history = []
    with open("conversions_history.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            conversion_history.append(row)
        return conversion_history

def reset_history_file(file_header: list) -> None:
    with open("conversions_history.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(file_header)

def init_history_file(file_header: list) -> list:
    if is_history_file_valid(file_header):
        return load_conversion_history()
    else:
        reset_history_file(file_header)
        return []


def is_history_file_valid(file_header: list) -> bool:
    try:
        with open("conversions_history.csv", "r", newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header != file_header:
                return False
            try:
                for row in reader:
                    float(row[1])
                    float(row[3])
                return True
            except (ValueError, IndexError):
                return False
    except FileNotFoundError:
        return False

def append_history_record(row: list) -> None:
    with open("conversions_history.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)


actions = {
    1: {
        "label": "Celsius → Fahrenheit",
        "func": celsius_to_fahrenheit,
        "in_unit": "Celsius",
        "out_unit": "Fahrenheit"
    },
    2: {
        "label": "Fahrenheit → Celsius",
        "func": fahrenheit_to_celsius,
        "in_unit": "Fahrenheit",
        "out_unit": "Celsius"
    },
    3: {
        "label": "Kelvin → Celsius",
        "func": kelvin_to_celsius,
        "in_unit": "Kelvin",
        "out_unit": "Celsius"
    },
    4: {
        "label": "Celsius → Kelvin",
        "func": celsius_to_kelvin,
        "in_unit": "Celsius",
        "out_unit": "Kelvin"
    },
    5: {
        "label": "Kelvin → Fahrenheit",
        "func": kelvin_to_fahrenheit,
        "in_unit": "Kelvin",
        "out_unit": "Fahrenheit"
    },
    6: {
        "label": "Fahrenheit → Kelvin",
        "func": fahrenheit_to_kelvin,
        "in_unit": "Fahrenheit",
        "out_unit": "Kelvin"
    },
    7: {
        "label": "KM → Miles",
        "func": km_to_miles,
        "in_unit": "KM",
        "out_unit": "Miles"
    },
    8: {
        "label": "Miles → KM",
        "func": miles_to_km,
        "in_unit": "Miles",
        "out_unit": "KM"
    },
    9: {
        "label": "KG → Pounds",
        "func": kg_to_pounds,
        "in_unit": "KG",
        "out_unit": "Pounds"
    },
    10: {
        "label": "Pounds → KG",
        "func": pounds_to_kg,
        "in_unit": "Pounds",
        "out_unit": "KG"
    },
    11: {
        "label": "Conversion History",
        "func": display_conversion_history,
        "required_input": False
    },
    0: {
        "label": "Exit",
        "func": None
    }
}


def get_choice(actions_dict):
    while True:
        print("\nAvailable options:")
        for key, action in actions_dict.items():
            print(f"{key}: {action['label']}")

        try:
            choice = int(input("Choose: "))
            if choice in actions_dict:
                return choice
            print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a number.")


def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def main():

    history_file_header = ["Input Unit", "Input Value", "Output Unit", "Result"]
    conversions_history = init_history_file(history_file_header)

    while True:
        choice = get_choice(actions)
        action = actions[choice]

        if action["func"] is None:
            print("Goodbye.")
            break

        elif action.get("required_input", True):
            value = get_numeric_input(f"Enter the value in {action['in_unit']}: ")
            result = action["func"](value)

            print(f"Result: {result:.2f} {action['out_unit']}")

            row = [action["in_unit"], value, action["out_unit"], result]
            conversions_history.append(row)
            append_history_record(row)
        else:
            display_conversion_history(conversions_history)


if __name__ == "__main__":
    main()