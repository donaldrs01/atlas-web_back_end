import Currency from './3-currency';

class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amountValue) {
    if (typeof amountValue !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = amountValue;
  }

  get currency() {
    return this._currency;
  }

  set currency(currencyValue) {
    if (!(currencyValue instanceof Currency)) {
      throw new TypeError('Currency must be an instance of the Currency class');
    }
    this._currency = currencyValue;
  }

  displayFullPrice() {
    return `${this.amount} ${this._currency.name} ${this._currency.code})`;
  }

  // static method that doesn't depend on any specific instance of 'Pricing' class
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Amount and conversion rate must be numbers');
    }
    return amount * conversionRate;
  }
}

export default Pricing;
