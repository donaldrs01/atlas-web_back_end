function calculateNumber(a, b) {
    const Around = Math.round(a);
    const Bround = Math.round(b);

    return Around + Bround;
}

module.exports = calculateNumber;