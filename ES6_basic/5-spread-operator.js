export default function concatArrays(array1, array2, string) {
  // spread syntax takes all elements of each object and combines them
  return [...array1, ...array2, ...string];
}
