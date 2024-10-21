const http = require("http");
const fs = require("fs");

const app = http.createServer((req, res) => {
    if (req.url === "/") {
        res.writeHead(200, {"Content-Type": "text/plain"});
        res.write("Hello Holberton School!");
        res.end()
    }
    else if (req.url === "/students") {
        const dbpath = process.argv[2]; // Grab db path from argument
        res.writeHead(200, {"Content-Type": "text/plain"});
        res.write("This is the list of our students:\n");
        // Declare fileContent variable to hold student data
        // Read the CSV file using async logic
        fs.readFile(dbpath, "utf-8", (err, fileContent) => {
            if (err) {
                res.write("Cannot load the database");
                res.end();
                return;
            }
            // Import logic from CSV file read
            const lines = fileContent.split("\n").filter(line => line.trim() !== "")
            // Store student data in object array
            const studentCounts = {};
            let totalStudents = 0;
            // Iterate through each line
            for (let index = 0; index < lines.length; index++) {
                const line = lines[index];
                const data = line.split(",");
                // Skip over header line and invalid data
                if (index === 0 || data.length < 4) continue;
                // Record valid student data
                const newStudent = {
                    firstName: data[0].trim(),
                    lastName: data[1].trim(),
                    age: data[2].trim(),
                    field: data[3].trim(),
                };
                    
                if (!studentCounts[newStudent.field]) {
                    // Initialize new array to hold students if new field entry
                    studentCounts[newStudent.field] = [];
                }
                studentCounts[newStudent.field].push(newStudent.firstName);
                totalStudents++
            }

            res.write(`Number of students: ${totalStudents}\n`);

            // Write number of students in each field
            for (const field in studentCounts) {
                const list = studentCounts[field].join(", ");
                res.write(`Number of students in ${field}: ${studentCounts[field].length}. List: ${list}\n`);
            }

            res.end();
        });
    }
});

app.listen(1245, () => {
    console.log("Server running on Port 1245");
});

module.exports = app;
