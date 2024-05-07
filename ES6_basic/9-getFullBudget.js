import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,  // spread syntax allows us to merge properties from 'budget' into 'fullBudget'
    getIncomeInDollars() {
        return `$${this.income}`; // holds income value extracted from budget object - displays as a string in dollars
    },
    getIncomeInEuros() {
        return `${this.income} euros`;
    },
  };
  return fullBudget;
}
