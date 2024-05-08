export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    // throw error if 0 entered as denominator
    throw new Error('cannot divide by 0');
  } else {
    return numerator / denominator;
  }
}
