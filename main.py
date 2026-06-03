from ConversionRecord import ConversionRecord
from ConversionsHistory import ConversionsHistory
from Action import Action


def get_choice(actions_dict: dict):
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

    conversions_history = ConversionsHistory()

    while True:
        choice = get_choice(Action.ACTIONS)
        action = Action(choice)

        if action.required_input:
            input_value = get_numeric_input(f"Enter the input_value in {action.in_unit}: ")
            result = action.fun(action,input_value)

            print(f"Result: {result:.2f} {action.out_unit}")

            record = ConversionRecord(action.in_unit,
                                      input_value,
                                      action.out_unit,
                                      result)
            conversions_history.append_record(record)
        else:
            try:
                action.fun(conversions_history)
            except StopIteration:
                break


if __name__ == "__main__":
    main()