# Time Calculator

## Overview
This project is a **Time Calculator**, developed as a mandatory requirement to claim the **Scientific Computing with Python** certification on **FreeCodeCamp**. It adds a given duration to a start time and returns the updated time in a 12-hour AM/PM format, along with the day of the week (if provided) and the number of days later (if applicable).

## Features
- Accepts a start time in **12-hour AM/PM format**.
- Adds a duration to the start time (hours and minutes).
- Returns the new time, adjusting for **AM/PM cycles**.
- Handles day transitions and **calculates the next day or days later**.
- Optionally accepts a weekday input and updates it accordingly.
- Provides formatted output for easy readability.
- **Edge Case Handling**:
  - Correctly manages overflows when minutes exceed 60.
  - Adjusts AM/PM cycles when hours exceed 12.
  - Calculates and tracks the number of days passed.

## How It Works
1. The function extracts hours, minutes, and AM/PM from the given start time.
2. It parses the duration and adds the hours and minutes accordingly.
3. Adjusts the time format to maintain a **12-hour clock**.
4. Computes the number of days passed if the total duration exceeds 24 hours.
5. If a weekday is provided, it calculates the updated day of the week.
6. Returns the final formatted time string.

## Usage
```python
print(add_time("8:16 PM", "466:02", "Tuesday"))
```
### Output:
```
6:18 AM, Monday (20 days later)
```

## Example Inputs & Outputs
| Start Time  | Duration  | Weekday  | Output  |
|-------------|-----------|----------|---------|
| 3:00 PM    | 3:10      | -        | 6:10 PM |
| 11:30 AM   | 2:32      | Monday   | 2:02 PM, Monday |
| 11:43 AM   | 00:20     | -        | 12:03 PM |
| 10:10 PM   | 3:30      | -        | 1:40 AM (next day) |
| 11:43 PM   | 24:20     | Tuesday  | 12:03 AM, Thursday (2 days later) |

## Installation & Running
No external libraries are required; this script runs with **Python 3+**.
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/time-calculator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd time-calculator
   ```
3. Run the script:
   ```sh
   python time_calculator.py
   ```

## Conclusion
This project effectively demonstrates **string manipulation, modular arithmetic, and logical decision-making** in Python. It enhances skills in handling **time calculations, conditional statements, and function structuring** while following clean coding practices.

---
✅ Completed as a part of the **Scientific Computing with Python** certification.

