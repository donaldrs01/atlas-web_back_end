class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  get code() {
    return this._code;
  }

  set code(codeValue) {
    if (typeof codeValue !== 'string') {
        throw new TypeError('Code must be a string');
    }
    this._code = codeValue;
  }

  get name() {
    return this._name;
  }

  set name(nameValue) {
    if (typeof nameValue !== 'string') {
        throw new TypeError('Name must be a string');
    }
    this._name = nameValue;
  }

  // Full currency method using template literal
  displayFullCurrency() {
    return `${this._name} (${this.code})`;
  }
}

