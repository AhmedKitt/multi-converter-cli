# Multi Converter CLI

A Python command-line application that converts between multiple unit categories including temperature, distance, and weight.

The application provides an interactive menu, validates user input, and persists conversion history using a CSV file.

---

## Features

### Temperature Conversions

- Celsius ↔ Fahrenheit
    
- Celsius ↔ Kelvin
    
- Fahrenheit ↔ Kelvin
    

### Distance Conversions

- Kilometers ↔ Miles
    

### Weight Conversions

- Kilograms ↔ Pounds
    

### Conversion History

- Save conversion history to a CSV file
    
- Load history automatically on startup
    
- Display previous conversions from within the application
    
- Validate the history file structure and contents
    
- Recreate the history file if it is missing or invalid
    

### Additional Features

- Interactive command-line interface
    
- Input validation using `try/except`
    
- Function-based architecture
    
- Dictionary-based action dispatching
    
- Persistent data storage using CSV
    

---

## Usage

Run the application:

```bash
python main.py
```

---

## Menu

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
11: Conversion History
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

## Conversion History Example

```text
1. KM 10.00 = Miles 6.21
2. Celsius 100.00 = Fahrenheit 212.00
```

---

## Project Structure

```text
.
├── main.py
├── README.md
├── .gitignore
└── conversions_history.csv
```
> Note: `conversions_history.csv` is generated automatically on first run and is ignored by Git.
---

## How It Works

- Each conversion is implemented as a dedicated function.
    
- Complex conversions reuse existing conversion functions.
    
- A dictionary (`actions`) maps menu selections to functions.
    
- User input is validated before processing.
    
- Conversion history is stored in a CSV file.
    
- History is loaded automatically when the program starts.
    

---

## Concepts Used

- Functions
    
- Dictionary dispatch tables
    
- File handling
    
- CSV processing
    
- Input validation
    
- Exception handling
    
- Modular design
    
- Data persistence
    

---

## Requirements

- Python 3.10+ (or Python 3.x)
    

---

## Development Roadmap

### Phase 1 (Completed)

- Temperature conversions
    
- Distance conversions
    
- Weight conversions
    
- Conversion history
    
- CSV persistence
    

### Phase 2 (Planned)

#### 1. Convert the application to OOP

- Introduce classes for converters
    
- Improve maintainability and scalability
    
- Separate business logic from application flow
    

#### 2. Add Unit Tests

- Test all conversion functions
    
- Test CSV history handling
    
- Improve reliability and prevent regressions
    

#### 3. Build a GUI

- Replace the CLI with a graphical interface
    
- Improve usability
    
- Provide a better user experience
    

---

## Author

Ahmad Kitana