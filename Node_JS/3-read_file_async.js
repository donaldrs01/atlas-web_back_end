const fs = require("node:fs/promises");

async function countStudents(path) {
    let fileContent;
    try {
        fileContent = await fs.readFile(path,"utf-8")
    } catch (error) {
        throw new Error("Cannot load the database");
    }
    // Split content into lines and filter out empty lines
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
        if (line !== "") {
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
