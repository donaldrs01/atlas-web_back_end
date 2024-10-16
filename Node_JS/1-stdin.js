// Reading user input using readline and displaying message
const readline = require("node:readline");

const { stdin: input, stdout: output } = require("node:process");

const r1 = readline.createInterface({input, output });

r1.question("Welcome to Holberton School, what is your name?\n", (answer) => {
    // Log answer and display to console
    console.log(`Your name is: ${answer}`);
    console.log("This important software is now closing");
    r1.close();
});