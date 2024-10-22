import Utils from "./utils.js";

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const res = Utils.calculateNumber("SUM", totalAmount, totalShipping);
    console.log(`The total price is: ${res}`);
}

module.exports = sendPaymentRequestToApi;