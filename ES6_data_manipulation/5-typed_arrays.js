export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  // create new arrayBuffer obj with given length
  const arrayBuffer = new ArrayBuffer(length);
  // create Int-8 type array out of ArrayBuffer
  const int8Array = new Int8Array(arrayBuffer);
  // set correct value
  int8Array[position] = value;

  return arrayBuffer;
}
