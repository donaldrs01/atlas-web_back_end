export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  // Casting into a Number returns the size
  valueOf() {
    return this._size;
  }

  // Casting into a String returns the location
  toString() {
    return this._location;
  }
}
