import Building from './5-building';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Calls parent class constructor for sqft attribute
    this._floors = floors;  
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return 'Evacuate slowly the ${this._floors} floors.';
  }
}

export default SkyHighBuilding;
