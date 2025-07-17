# 🤖 Robot Simulation on a Grid

This project simulates multiple robots moving on a grid terrain based on directional inputs like `N3`, `E2`, etc. Each robot has a unique ID, starts at position `(0, 0)`, and moves based on input commands unless another robot is already occupying the destination cell.

---

## 📌 Problem Statement

A robot listens to inputs and makes movements based on the input. Such an input can only be a two-letter input.

- The first character of the input refers to the direction:
  - `N` - North
  - `S` - South
  - `E` - East
  - `W` - West
- The second character (or number) refers to the number of steps.

### ✅ Requirements Implemented

- Create multiple robots.
- Assign each robot a unique number.
- Move a selected robot based on input.
- Prevent a robot from entering a cell already occupied by another robot.
- Display the current location of any robot.
- Terrain is a grid of rows and columns.
- Robots always start from cell `(0, 0)`.
- Terrain doesn't need to be visually represented.
- Unit tests included using Python’s `unittest`.

---

## 📁 Project Structure

robot-simulation/
├── robot.py # Core logic: Robot and Terrain classes
├── main.py # Sample usage of robot movement
├── test_robot.py # Unit tests using unittest
├── requirements.txt # Python dependencies
└── README.md # Project info and instructions



---

## 🚀 How to Run

### 1. Clone the Repository

```bash

git clone https://github.com/your-username/robot-simulation.git
cd robot-simulation


### Step 2: Run the Code Manually (main.py)

You can test robot movement manually using `main.py`.

To run it:

```bash
python main.py
```

**Expected output example:**

Move Robot 1: (0, 5)
Move Robot 2: (0, 4)
Robot 1 Position: (0, 5)
Robot 2 Position: (0, 4)

This means Robot 1 moved East 5 steps to (0, 5), and Robot 2 stopped at (0, 4) to avoid collision.


### Step 3: Run the Unit Tests

This will automatically check if your robot logic is working correctly.

To run the tests:

```bash
python test_robot.py 
or
python -m unittest test_robot.py


```

**Expected output:**

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

If you see `OK`, your code is correct!

------


## 🛠 Requirements

* Python 3.6 or higher
* No third-party packages required (only built-in modules)
