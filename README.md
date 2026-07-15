# UENR Student CGPA & Target Predictor CLI Application

 A multi-file Python Command Line Interface (CLI) application built for students at the University of Energy and Natural Resources (UENR), Ghana. This tool allows students to log course records, track their ongoing cumulative GPA (CGPA), and predict future grade targets necessary for their desired graduation class.

## Project Structure
- `main.py`: Houses the interactive menu, input sanitization, and terminal loop.
- `gpa_calc.py`: Contains modular arithmetic functions tracking credit allocations and predictive GPA equations.
- `data_handler.py`: Manages persistence data using structured file system serialization (`.json`).

## How to Run
Ensure Python 3 is installed. Navigate to the project directory and execute:
```bash
python main.py
```



