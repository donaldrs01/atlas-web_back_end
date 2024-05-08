export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  // create new map to return with updated values
  // const updatedMap = new Map();

  for (const [key, value] of map) {
    if (value === 1) {
      // update value to 100 if originally set to 1
      map.set(key, 100);
    } else {
      map.set(key, value);
    }
  }
  return map;
}
