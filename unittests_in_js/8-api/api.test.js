const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');


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