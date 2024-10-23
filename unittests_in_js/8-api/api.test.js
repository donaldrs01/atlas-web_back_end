const axios = require('axios');
const { expect } = require('chai');

describe('API index page test', () => {
    const url = 'http://localhost:7865/';

    it('should return 200 status code', async () => {
        // async/await to pause test execution until the get request finishes
        const response = await axios.get(url);
        expect(response.status).to.equal(200);
    });

    it('should return the correct message', async () => {
        const response = await axios.get(url);
        expect(response.data).to.equal('Welcome to the payment system');
    });
});