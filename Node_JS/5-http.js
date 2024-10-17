const http = require("http");
const countStudents = require("./3-read_file_async");

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
        // use countStudents function
        countStudents(dbpath)
            .then((output) => {
                res.write(`${output}\n`);  // Print student info
                res.end();
            })
            .catch((error) => {
                res.end("Cannot load the database");
            });
    }
});

app.listen(1245, () => {
    console.log("Server running on Port 1245");
});

module.exports = app;
