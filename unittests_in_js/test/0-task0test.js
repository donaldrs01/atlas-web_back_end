const assert = require("assert");
const calculateNumber = require("../0-calcul");

describe("calculateNumber", function () {
    it("should return rounded sum of both numbers", function () {
        assert.equal(calculateNumber(4.2, 7.8), 12);
        assert.equal(calculateNumber(1.1, 3.2), 4);
        assert.equal(calculateNumber(-6.4, -3.2), -9);
    });
});