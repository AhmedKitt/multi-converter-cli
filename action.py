"""
Action registry — maps menu keys to labels, converter functions, and units.
Kept as plain data (no class needed).
"""
import converters

# Each entry:
#   label         : displayed in the menu
#   func          : callable(value) -> float   (None for non-conversion actions)
#   in_unit       : input unit label
#   out_unit      : output unit label
#   requires_input: flag of conversion actions
#   exit          : exit flag

ACTIONS: dict[int, dict] = {
    1: {
        "label": "Celsius → Fahrenheit",
        "func": converters.celsius_to_fahrenheit,
        "in_unit": "Celsius",
        "out_unit": "Fahrenheit"
    },
    2: {
        "label": "Fahrenheit → Celsius",
        "func": converters.fahrenheit_to_celsius,
        "in_unit": "Fahrenheit",
        "out_unit": "Celsius"
    },
    3: {
        "label": "Kelvin → Celsius",
        "func": converters.kelvin_to_celsius,
        "in_unit": "Kelvin",
        "out_unit": "Celsius"
    },
    4: {
        "label": "Celsius → Kelvin",
        "func": converters.celsius_to_kelvin,
        "in_unit": "Celsius",
        "out_unit": "Kelvin"
    },
    5: {
        "label": "Kelvin → Fahrenheit",
        "func": converters.kelvin_to_fahrenheit,
        "in_unit": "Kelvin",
        "out_unit": "Fahrenheit"
    },
    6: {
        "label": "Fahrenheit → Kelvin",
        "func": converters.fahrenheit_to_kelvin,
        "in_unit": "Fahrenheit",
        "out_unit": "Kelvin"
    },
    7: {
        "label": "KM → Miles",
        "func": converters.km_to_miles,
        "in_unit": "KM",
        "out_unit": "Miles"
    },
    8: {
        "label": "Miles → KM",
        "func": converters.miles_to_km,
        "in_unit": "Miles",
        "out_unit": "KM"
    },
    9: {
        "label": "KG → Pounds",
        "func": converters.kg_to_pounds,
        "in_unit": "KG",
        "out_unit": "Pounds"
    },
    10: {
        "label": "Pounds → KG",
        "func": converters.pounds_to_kg,
        "in_unit": "Pounds",
        "out_unit": "KG"
    },
    11: {
        "label": "Conversion History",
        "func": None,
        "required_input": False
    },
    0: {
        "label": "Exit",
        "func": None,
        "required_input": False,
        "exit": True
    }
}
