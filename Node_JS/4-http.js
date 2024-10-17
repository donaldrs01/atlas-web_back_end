const http = require("http");

// Create HTTP server
const app = http.createServer((req, res) => {
    res.write("Hello Holberton School!"); // write resposne to client
    res.end();
}).listen(1245)

module.exports = app;
