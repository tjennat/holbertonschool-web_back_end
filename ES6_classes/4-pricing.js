/* eslint-disable */
import Currency from "./3-currency.js";

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount(){
    return this._amount;
  }

  set amount(newAmount){
    this._amount = newAmount;
  }

  get currency(){
    return this._currency;
  }

  set currency(newCurrency){
    this._currency = newCurrency;
  }

  displayFullPrice() {
    const { _name, _code } = this._currency;
    return `${this._amount} ${_name} (${_code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
