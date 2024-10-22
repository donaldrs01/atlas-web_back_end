const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./3-payment.js");

describe("sendPaymentRequestToApi", function () {
    beforeEach(function () {
        // Wrap method in a spy
        sinon.spy(Utils, "calculateNumber");
    });

    afterEach(function() {
        sinon.restore();
    });

    it("should call calculateNumber and match the sendPayment result", function () {
        // Call function to test
        sendPaymentRequestToApi(100,20);

        // Verify calculateNumber called one time
        expect(Utils.calculateNumber.calledOnce).to.be.true;

        // Verify called with correct arguments
        expect(Utils.calculateNumber.calledWithExactly("SUM", 100, 20)).to.be.true;
    });
});