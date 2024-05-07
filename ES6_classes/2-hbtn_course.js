class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name; // call 'name' setter for type validation
    this._length = length;
    this.students = students;
  }
  // Getter / setter methods for 'name' property
  get name() {
    return this._name;
  }
  set name(nameValue) {
    if (typeof nameValue !== 'string') {
        throw new TypeError('Name must be a string');
    }
    this._name = nameValue;
  }

  // Getter / setter methods for 'length' property
  get length() {
    return this._length;
  }
  set length(lengthValue) {
    if (typeof lengthValue !== 'number') {
        throw new TypeError('Length must be a number');
    }
    this._length = lengthValue;
  }

  // Getter / setter methods for 'students' property
  get students() {
    return this._students;
  }
  set students(studentsValue) {
    this._students = studentsValue;
    }
}

export default HolbertonCourse;