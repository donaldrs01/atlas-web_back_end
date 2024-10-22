const Utils = {
    calculateNumber(type, a, b) {
        const Around = Math.round(a);
        const Bround = Math.round(b);
    
        // Perform operation based on type input
        if (type === "SUM") {
            return Around + Bround;
        } else if (type === "SUBTRACT") {
            return Around - Bround;
        } else if (type === "DIVIDE") {
            if (Bround === 0) {
                return "Error";
            }
            return Around / Bround;
        }
    }
};

export default Utils;