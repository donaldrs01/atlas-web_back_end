export default function hasValuesFromArray(set, array) {
  // 'every' array method returns boolean if set has identical values
  return array.every((value) => set.has(value));
}
