# Multi Converter CLI

A simple and interactive command-line application written in Python for converting between multiple unit types including temperature, distance, and weight.

The program provides a clean user interface, validates user input, and demonstrates a modular and maintainable code structure.

---

## Features

### Temperature Conversions
- Celsius ↔ Fahrenheit
- Celsius ↔ Kelvin
- Fahrenheit ↔ Kelvin

### Distance Conversions
- KM ↔ Miles

### Weight Conversions
- KG ↔ Pounds

### Additional Features
- Interactive command-line menu
- Input validation using `try/except`
- Modular and reusable conversion functions
- Dictionary-based action mapping

---

## Usage

Run the program using:

```bash
python main.py
```

---

## Menu Example

```text
Available options:
1: Celsius → Fahrenheit
2: Fahrenheit → Celsius
3: Kelvin → Celsius
4: Celsius → Kelvin
5: Kelvin → Fahrenheit
6: Fahrenheit → Kelvin
7: KM → Miles
8: Miles → KM
9: KG → Pounds
10: Pounds → KG
0: Exit
```

---

## Example

```text
Choose: 7
Enter the value in KM: 10
Result: 6.21 Miles
```

---

## Project Structure

```text
.
├── main.py
├── README.md
└── .gitignore
```

---

## How It Works

- Each conversion type is implemented as a separate function
- More complex conversions reuse simpler conversion functions
- A dictionary (`actions`) maps menu choices to functions
- Input is validated to prevent invalid numeric input
- The application runs continuously until the user exits

---

## Concepts Used

- Functional programming
- Dictionary-based function dispatching
- Input validation and exception handling
- Separation of logic from user interaction
- Code reuse and modular design

---

## Requirements

- Python 3.x

---

## Changelog

### feat: add distance and weight conversions
- Add KM ↔ Miles conversion support
- Add KG ↔ Pounds conversion support
- Generalize input handling using `get_value`
- Transform project into multi-unit converter

### feat: support Kelvin conversions
- Add Kelvin conversion functions
- Extend CLI menu options
- Improve coverage of temperature units

### feat: add temperature conversion CLI
- Add Celsius and Fahrenheit conversion functions
- Implement interactive menu using dictionary
- Handle invalid input using `try/except`

### initial project setup
- Initialize repository
- Add base project files

---

## Author

Ahmad Kitana

---

## Future Improvements

- Add more conversion categories
  - Length
  - Area
  - Volume
  - Speed
- Add validation for physical constraints
- Support command-line arguments using `argparse`
- Add unit tests
- Convert project into installable CLI tool