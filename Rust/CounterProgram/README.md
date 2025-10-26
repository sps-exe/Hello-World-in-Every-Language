# Simple Counter Program in Rust

A simple command-line interface (CLI) counter program written in Rust that allows users to increase, decrease, or exit the counter.

## Description

This program demonstrates basic Rust programming concepts including:
- User input handling
- Pattern matching
- Loop control flow
- Integer arithmetic
- Console I/O operations

## Prerequisites

Before running this program, you need to have Rust installed on your system.

### Installing Rust

1. **Linux, macOS, or Unix-like OS:**
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

2. **Windows:**
   - Download and run the installer from [rustup.rs](https://rustup.rs/)
   - Follow the on-screen instructions

3. **Verify Installation:**
   ```bash
   rustc --version
   ```

## Setup

1. Clone this repository or download the `counter.rs` file

2. Navigate to the directory containing `counter.rs`:
   ```bash
   cd path/to/Rust/CounterProgram
   ```

## How to Run

### Option 1: Compile and Run Separately

1. **Compile the program:**
   ```bash
   rustc counter.rs
   ```

2. **Run the compiled executable:**
   - On Linux/macOS:
     ```bash
     ./counter
     ```
   - On Windows:
     ```cmd
     counter.exe
     ```

### Option 2: Compile and Run in One Step

```bash
rustc counter.rs && ./counter
```

On Windows:
```cmd
rustc counter.rs && counter.exe
```

## Usage

Once the program is running:

1. The program will display the current counter value (starting at 0)
2. You will be presented with three options:
   - Enter `1` to increase the counter by 1
   - Enter `2` to decrease the counter by 1
   - Enter `3` to exit the program
3. The program will continue running until you choose to exit
4. Upon exit, it will display the final counter value

### Example Session

```
Simple Counter Program
======================

Current Counter: 0

Options:
1. Increase (+1)
2. Decrease (-1)
3. Exit

Enter your choice (1-3): 1

✓ Counter increased!

Current Counter: 1

Options:
1. Increase (+1)
2. Decrease (-1)
3. Exit

Enter your choice (1-3): 1

✓ Counter increased!

Current Counter: 2

Options:
1. Increase (+1)
2. Decrease (-1)
3. Exit

Enter your choice (1-3): 2

✓ Counter decreased!

Current Counter: 1

Options:
1. Increase (+1)
2. Decrease (-1)
3. Exit

Enter your choice (1-3): 3

Exiting... Final counter value: 1
Thank you for using the counter program!
```

## Features

- ✅ Simple and intuitive CLI interface
- ✅ Increment counter functionality
- ✅ Decrement counter functionality
- ✅ Input validation with error messages
- ✅ Clean exit with final value display
- ✅ Continuous operation until user exits

## Troubleshooting

**Issue:** `rustc: command not found`
- **Solution:** Make sure Rust is properly installed and added to your PATH. Restart your terminal after installation.

**Issue:** Permission denied when running `./counter`
- **Solution:** Make the file executable:
  ```bash
  chmod +x counter
  ```

**Issue:** Program doesn't respond to input
- **Solution:** Make sure to press Enter after typing your choice.

## Contributing

This program was created for Issue #68 of the Hello-World-in-Every-Language repository. Feel free to suggest improvements!

## License

This project is part of the Hello-World-in-Every-Language repository.
