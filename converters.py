"""
Pure conversion functions — no class needed, just math.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    _require_non_negative_kelvin(celsius + 273.15)
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    _require_non_negative_kelvin(fahrenheit + 459.67)
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin: float) -> float:
    _require_non_negative_kelvin(kelvin)
    return kelvin - 273.15

def celsius_to_kelvin(celsius: float) -> float:
    kelvin = celsius + 273.15
    _require_non_negative_kelvin(kelvin)
    return kelvin

def kelvin_to_fahrenheit(kelvin: float) -> float:
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def km_to_miles(km: float) -> float:
    _require_positive(km, "Distance")
    miles = km / 1.609344
    return miles

def miles_to_km(miles: float) -> float:
    _require_positive(miles, "Distance")
    km = miles * 1.609344
    return km

def kg_to_pounds(kg: float) -> float:
    _require_positive(kg, "Weight")
    pounds = kg * 2.20462
    return pounds

def pounds_to_kg(pounds: float) -> float:
    _require_positive(pounds, "Weight")
    kg = pounds / 2.20462
    return kg

def _require_positive(value: float, label: str) -> None:
    if value < 0:
        raise ValueError(f'"{label}" cannot be negative.')

def _require_non_negative_kelvin(value: float) -> None:
    if value < 0:
        raise ValueError("Temperature cannot be below absolute zero.")