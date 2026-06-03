from ConversionsHistory import ConversionsHistory

class Action:
    def __init__(self, action_code):
        self._action = self.ACTIONS[action_code]
        self.label = self._action["label"]
        self.fun = self._action["func"]
        self.in_unit = self._action.get("in_unit", None)
        self.out_unit = self._action.get("out_unit", None)
        self.required_input = self._action.get("required_input", True)


    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9

    def kelvin_to_celsius(self, kelvin: float) -> float:
        return kelvin - 273.15

    def celsius_to_kelvin(self, celsius: float) -> float:
        return celsius + 273.15

    def kelvin_to_fahrenheit(self, kelvin: float) -> float:
        celsius = self.kelvin_to_celsius(kelvin)
        return self.celsius_to_fahrenheit(celsius)

    def fahrenheit_to_kelvin(self, fahrenheit: float) -> float:
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)

    def km_to_miles(self, km: float) -> float:
        miles = km / 1.609344
        return miles

    def miles_to_km(self, miles: float) -> float:
        km = miles * 1.609344
        return km

    def kg_to_pounds(self, kg: float) -> float:
        pounds = kg * 2.20462
        return pounds

    def pounds_to_kg(self, pounds: float) -> float:
        kg = pounds / 2.20462
        return kg

    def display_conversion_history(conversions_history: ConversionsHistory) -> None:
        print(conversions_history)

    # use temp just to allow to call it with an attribute because this method called in same
    # line of 'display_conversion_history'
    def exit_from_program(temp) -> None:
        print("Goodbye.")
        raise StopIteration

    ACTIONS = {
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
            "func": exit_from_program,
            "required_input": False
        }
    }
