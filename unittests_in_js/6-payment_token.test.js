const { expect } = require("chai");
const getPaymentTokenFromApi = require('./6-payment_token');

describe('getPaymentTokenFromApi', function () {
    const expectedResponse = { data: 'Successful response from the API' };
    // Checks that a true return (success) correctly logs data
    it('should return a resolved promise with { data: "Successful response from the API" }', function (done) {
        getPaymentTokenFromApi(true)
            .then((response) => {
                // Deep equal better for comparing objects / arrays
                expect(response).to.deep.equal(expectedResponse);
                done();
            })
    });
});