const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

// Regex to force ID to be number only
app.get('/cart/:id(\\d+)', (req, res) => {
    const id = req.params.id;
    res.status(200).send(`Payment methods for cart ${id}`);
});

module.exports = app;

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});