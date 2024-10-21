const express = require("express");
const fs = require("fs").promises

const app = express();
const port = 1245;

// Define the "/" route
app.get("/", (req, res) => {
    res.send("Hello Holberton School!");
});

// Define "students" route
app.get("/students", async (req, res) => {
    const dbPath = process.argv[2];

    if (!dbPath) {
        res.status(400).send("Missing database argument");
        return;
    }

    try {
        // Await reading file content until processing completes
        const fileContent = await fs.readFile(dbPath, "utf-8");

        // Parse through file content
        const lines = fileContent.split("\n").filter(line => line.trim() !== "");
        const studentCounts = {};
        let totalStudents = 0;
        // Start at index 1 to skip header line
        for (let index = 1; index < lines.length; index++) {
            const data = lines[index].split(",");
            if (data.length < 4) continue;

            const newStudent = {
                firstName: data[0].trim(),
                lastName: data[1].trim(),
                age: data[2].trim(),
                field: data[3].trim(),
            };

            if (!studentCounts[newStudent.field]) {
                studentCounts[newStudent.field] = [];
            }
            studentCounts[newStudent.field].push(newStudent.firstName);
            totalStudents++;
        }

        // Result string
        let result = `Number of students: ${totalStudents}\n`;
        for (const field in studentCounts) {
            const list = studentCounts[field].join(", ");
            result += `Number of students in ${field}: ${studentCounts[field].length}. List: ${list}\n`;
        }
        // Send back response with parsed data
        res.status(200).send(`This is the list of our students\n${result}`);
    } catch (error) {
        // Error handling
        res.status(500).send("Cannot load database");
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

module.exports = app;