export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  // create new map to return with updated values
  const updatedMap = new Map();

  for (const [key, value] of map) {
    if (value === 1) {
      // update value to 100 if originally set to 1
      updatedMap.set(key, 100);
    } else {
      updatedMap.set(key, value);
    }
  }
  return updatedMap;
}
