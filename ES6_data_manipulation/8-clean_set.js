export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string')
    {
        return '';
    }
  const valueMatch = [];
  for (const value of set) {
    // use startsWith string method
    if (value.startsWith(startString)) {
        // Append remaining part of string to valueMatch by moving length of input string
        valueMatch.push(value.slice(startString.length));
    }
  }
  const listValues = valueMatch.join('-');

  return listValues;
}
