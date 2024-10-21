const assert = require("assert");
const calculateNumber = require("../1-calcul");

describe("calculateNumber", function () {
    it("should return rounded sum when type is SUM", function () {
        assert.equal(calculateNumber("SUM", 4.6, 1.2), 6);
        assert.equal(calculateNumber("SUM", 9.8, 2.4), 12);
    });

    it("should return difference of rounded numbers when type is SUBTRACT", function () {
        assert.equal(calculateNumber("SUBTRACT", 5.3, 1.1), 4);
        assert.equal(calculateNumber("SUBTRACT", 10.1, 7.8), 2);
    });

    it("should return the division of two rounded numbers when type is DIVIDE", function () {
        assert.equal(calculateNumber("DIVIDE", 4.4, 2.2), 2);
        assert.equal(calculateNumber("DIVIDE", 12.3, 4.4), 3);
    });

    it("should return Error when second number is 0", function () {
        assert.equal(calculateNumber("DIVIDE", 4.4, 0.3), "Error");
        assert.equal(calculateNumber("DIVIDE", 12.3, 0.1), "Error");
    });
});