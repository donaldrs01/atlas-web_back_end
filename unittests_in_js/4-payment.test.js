const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./4-payment.js");

describe("sendPaymentRequestToApi", function () {
    let stub;
    let spy;

    beforeEach(function () {
        // Stub calculateNumber to always return 10
        stub = sinon.stub(Utils, "calculateNumber").returns(10);
        // Spy on log message
        spy = sinon.spy(console, "log");
    });

    afterEach(function() {
        sinon.restore();
    });

    it("should call calculateNumber with expected arguments", function () {
        // Call function to test
        sendPaymentRequestToApi(100,20);

        // Verify that stub was called with expected arguments
        expect(stub.calledOnceWithExactly("SUM", 100, 20)).to.be.true;

        // Verify that console log reads correct message
        expect(spy.calledOnceWithExactly("The total is: 10")).to.be.true;
    });
});