from ConversionRecord import ConversionRecord
from ConversionHistory import ConversionHistory
from action import ACTIONS


def get_choice() -> int:
    """Show the menu and return a valid action key."""
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

def get_numeric_input(prompt: str) -> float:
    """Ask for a float, retry on bad input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

# Main loop
def main():
    conversions_history = ConversionHistory()

    while True:
        choice = get_choice()
        action = ACTIONS[choice]

        # Conversion actions
        if action.get("required_input", True):
            input_value = get_numeric_input(f"Enter the input_value in {action['in_unit']}: ")
            try:
                result = action["func"](input_value)
                print(f"Result: {result:.2f} {action['out_unit']}")

                record = ConversionRecord(action['in_unit'],
                                          input_value,
                                          action['out_unit'],
                                          result)
                conversions_history.append_record(record)
            except ValueError as e:
                print(f"Error: {e}") # Display validation error message.
        # Non - conversion actions
        elif action.get("exit", False): # Exit
            break
        else: # Display Conversion History
            print(conversions_history)

if __name__ == "__main__":
    main()