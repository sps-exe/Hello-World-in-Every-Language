# Interactive Counter Program in JavaScript

## Description

This is an interactive command-line counter program built with Node.js. It allows users to increase or decrease a counter value by 1 through a simple menu-driven interface. The program continues running until the user chooses to exit.

## Features

- **Increase Counter**: Increment the counter value by 1
- **Decrease Counter**: Decrement the counter value by 1
- **Interactive Menu**: User-friendly menu interface with clear options
- **Real-time Display**: Shows the current counter value after each operation
- **Exit Option**: Allows users to exit the program gracefully and displays the final counter value

## Prerequisites

- Node.js installed on your system (version 10.0 or higher recommended)

## How to Run

1. Make sure you have Node.js installed on your system. You can check by running:
   ```bash
   node --version
   ```

2. Navigate to the directory containing `counter.js`:
   ```bash
   cd JavaScript/CounterProgram
   ```

3. Run the program using Node.js:
   ```bash
   node counter.js
   ```

## Usage

Once the program starts, you'll see an interactive menu:

```
=== Interactive Counter Program ===
Welcome! This program allows you to increase or decrease a counter.

========================
Current Counter: 0
========================
1. Increase counter by 1
2. Decrease counter by 1
3. Exit
========================
Enter your choice (1-3):
```

- Press `1` and hit Enter to increase the counter
- Press `2` and hit Enter to decrease the counter
- Press `3` and hit Enter to exit the program

## Example Session

```
Current Counter: 0
Enter your choice (1-3): 1
Counter increased to: 1

Current Counter: 1
Enter your choice (1-3): 1
Counter increased to: 2

Current Counter: 2
Enter your choice (1-3): 2
Counter decreased to: 1

Current Counter: 1
Enter your choice (1-3): 3

Final counter value: 1
Thank you for using the Counter Program!
```

## Implementation Details

- Uses Node.js built-in `readline` module for interactive input
- Counter starts at 0 by default
- Supports negative numbers (counter can go below 0)
- Input validation to handle invalid menu choices

## Author

Created as part of the Hello-World-in-Every-Language project.

## Related Issue

This program addresses Issue #69: Create an Interactive Counter Program in JavaScript with a Clear README
