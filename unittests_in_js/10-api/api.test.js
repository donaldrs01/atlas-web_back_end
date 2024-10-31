const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');
const { it } = require('node:test');


describe('API index page test', () => {
    it('should return 200 status code', (done) => {
        // Request to make GET request to app
        request(app)
            .get('/') // endpoint being tested
            .expect(200) // status code to expect
            .end((err, res) => {
                if (err) return done(err); // fail test if error
                done();
            });
    });

    it('should return correct message', (done) => {
        request(app)
            .get('/')
            .end((err, res) => {
                if (err) return done(err);
                // Expect test to verify response text matches expected output
                expect(res.text).to.equal('Welcome to the payment system');
                done();
            });
    });
});

describe('Cart page', () => {
    it('should return status code 200 when ID is a number', (done) => {
        request(app)
            .get('/cart/555')
            .expect(200)
            .expect('Payment methods for cart 555', done);
    });

    it('should return status code 404 when ID is not a number', (done) => {
        request(app)
            .get('/cart/abc')
            .expect(404, done);
    });

    it('should return status code 404 when no ID is provided', (done) => {
        request(app)
            .get('/cart/')
            .expect(404, done);
    });
});

describe('GET /available_payments', function () {
    it('should return proper object with correct JSON data', function (done) {
        request(app)
            .get('/available_payments')
            .expect(200)
            .end((err, res) => {
                if (err) return done(err);
                expect (res.body).to.deep.equal({
                    payment_methods: {
                        credit_cards: true,
                        paypal: false,
                    },
                });
                done();
            });
    });
});

describe('POST /login', () => {
    it('should return message with correct userName', async () => {
        const response = await request(app)
            .post('/login')
            .send({ userName: 'Betty'})
            .set('Content-Type', 'application/json');
        expect(response.status).to.equal(200);
        expect(response.text).to.equal('Welcome Betty');
    });

    it('should return 400 error if no userName provided', async () => {
        const response = await request(app)
            .post('/login')
            .send({}) // empty input
            .set('Content-Type', 'application/json');
        expect(response.status).to.equal(400);
        expect(response.body).to.deep.equal({ error: 'No username provided' });
    });
});