class Building {
  constructor(sqft) {
    // Abstract class - issues warning if not an instance of Building class
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
export default Building;
