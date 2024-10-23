const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./5-payment.js");

describe("sendPaymentRequestToApi", function () {
    let spy;

    // Set up spy before each test
    beforeEach(function () {
        spy = sinon.spy(console, "log");
    });

    // Clear spy after each test
    afterEach(function () {
        spy.restore();
    });

    it('should log "The total is: 120" when sent correct arguments', function () {
        sendPaymentRequestToApi(100,20);
        expect(spy.calledOnce).to.be.true;
        expect(spy.calledWith('The total is: 120')).to.be.true;
    });

    it('should log "the total is: 20" when sent correct arguments', function () {
        sendPaymentRequestToApi(10,10);
        expect(spy.calledOnce).to.be.true;
        expect(spy.calledWith('The total is: 20')).to.be.true;
    });
});