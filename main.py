from ConversionRecord import ConversionRecord
from ConversionsHistory import ConversionsHistory
from action import ACTIONS


def get_choice():
    while True:
        print("\nAvailable options:")
        for key, action in ACTIONS.items():
            print(f"{key}: {action['label']}")

        try:
            choice = int(input("Choose: "))
            if choice in ACTIONS:
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

    conversions_history = ConversionsHistory()

    while True:
        choice = get_choice()
        action = ACTIONS[choice]

        if action.get("required_input", True):
            input_value = get_numeric_input(f"Enter the input_value in {action['in_unit']}: ")
            result = action["func"](input_value)

            print(f"Result: {result:.2f} {action['out_unit']}")

            record = ConversionRecord(action['in_unit'],
                                      input_value,
                                      action['out_unit'],
                                      result)
            conversions_history.append_record(record)
        elif action.get("exit", False):
            break
        else:
            print(conversions_history)




if __name__ == "__main__":
    main()