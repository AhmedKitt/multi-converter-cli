"""
Pure conversion functions — no class needed, just math.
"""

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
