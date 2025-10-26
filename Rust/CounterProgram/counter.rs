use std::io::{self, Write};

fn main() {
    let mut counter: i32 = 0;

    println!("Simple Counter Program");
    println!("======================\n");

    loop {
        println!("\nCurrent Counter: {}", counter);
        println!("\nOptions:");
        println!("1. Increase (+1)");
        println!("2. Decrease (-1)");
        println!("3. Exit");
        print!("\nEnter your choice (1-3): ");
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");

        let choice = input.trim();

        match choice {
            "1" => {
                counter += 1;
                println!("\n✓ Counter increased!");
            }
            "2" => {
                counter -= 1;
                println!("\n✓ Counter decreased!");
            }
            "3" => {
                println!("\nExiting... Final counter value: {}", counter);
                println!("Thank you for using the counter program!");
                break;
            }
            _ => {
                println!("\n✗ Invalid choice! Please enter 1, 2, or 3.");
            }
        }
    }
}
