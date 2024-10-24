// countStudents function that reads CSV file, counts # of students, and logs to console
// Implement fs module to read file
const fs = require("fs");

function countStudents(path) {
    let file_content;
    try {
        file_content = fs.readFileSync(path, "utf-8");
    } catch (error) {
        throw new Error("Cannot load the database");
    }
    // Split content into lines and filter out empty lines
    const lines = file_content.split("\n").filter(line => line.trim() !== "")
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
        if (line !== "") {
            const newStudent = {
                firstName: data[0].trim(), // Trim the whitespace
                lastName: data[1].trim(),
                age: data[2].trim(),
                field: data[3].trim(),
            };
            // Count the students by their field
            // Check whether field property exists for student
            if (!studentCounts[newStudent.field]) {
                // Initialize empty array to hold students in new field
                studentCounts[newStudent.field] = [];
            }
            // Add student's first name to corresponding field array
            studentCounts[newStudent.field].push(newStudent.firstName);
            // Increment student count
            totalStudents++
        }
    }

    // Log total number of students
    console.log(`Number of students: ${totalStudents}`);
    // Log number of students in each field
    for (const field in studentCounts) {
        const list = studentCounts[field].join(", ");
        console.log(`Number of students in ${field}: ${studentCounts[field].length}. List: ${list}`);
    }
} 

module.exports = countStudents;