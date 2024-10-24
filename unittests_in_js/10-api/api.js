const express = require('express');
const app = express();
const port = 7865;

// Allow to parse JSON request 
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

// Regex to force ID to be number only
app.get('/cart/:id(\\d+)', (req, res) => {
    const id = req.params.id;
    res.status(200).send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
    res.json ({
        payment_methods: {
            credit_cards: true,
            paypal: false,
        },
    });
});

app.post('/login', (req, res) => {
    const { userName} = req.body;
    if (!userName) {
        return res.status(400).json({ error: 'No username provided'});
    } else {
        res.send(`Welcome ${userName}`);
    }
});

module.exports = app;

app.listen(port, () => {
    console.log(`API on localhost port ${port}`);
});