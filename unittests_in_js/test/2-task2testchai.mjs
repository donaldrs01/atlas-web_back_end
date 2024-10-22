import { expect }  from "chai";
import calculateNumber from "../2-calcul_chai.js";

describe("calculateNumber", function () {
    it("should return rounded sum when type is SUM", function () {
        expect(calculateNumber("SUM", 4.6, 1.2)).to.equal(6);
        expect(calculateNumber("SUM", 9.8, 2.4)).to.equal(12);
    });

    it("should return difference of rounded numbers when type is SUBTRACT", function () {
        expect(calculateNumber("SUBTRACT", 5.3, 1.1)).to.equal(4);
        expect(calculateNumber("SUBTRACT", 10.1, 7.8)).to.equal(2);
    });

    it("should return the division of two rounded numbers when type is DIVIDE", function () {
        expect(calculateNumber("DIVIDE", 4.4, 2.2)).to.equal(2);
        expect(calculateNumber("DIVIDE", 12.3, 4.4)).to.equal(3);
    });

    it("should return Error when second number is 0", function () {
        expect(calculateNumber("DIVIDE", 4.4, 0.3)).to.equal("Error");
        expect(calculateNumber("DIVIDE", 12.3, 0.1)).to.equal("Error");
    });
});