const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let counter = 0;

function displayMenu() {
  console.log('\n========================');
  console.log(`Current Counter: ${counter}`);
  console.log('========================');
  console.log('1. Increase counter by 1');
  console.log('2. Decrease counter by 1');
  console.log('3. Exit');
  console.log('========================');
}

function handleChoice(choice) {
  switch (choice.trim()) {
    case '1':
      counter++;
      console.log(`Counter increased to: ${counter}`);
      promptUser();
      break;
    case '2':
      counter--;
      console.log(`Counter decreased to: ${counter}`);
      promptUser();
      break;
    case '3':
      console.log(`\nFinal counter value: ${counter}`);
      console.log('Thank you for using the Counter Program!');
      rl.close();
      break;
    default:
      console.log('Invalid choice. Please enter 1, 2, or 3.');
      promptUser();
      break;
  }
}

function promptUser() {
  displayMenu();
  rl.question('Enter your choice (1-3): ', handleChoice);
}

console.log('\n=== Interactive Counter Program ===');
console.log('Welcome! This program allows you to increase or decrease a counter.\n');
promptUser();
