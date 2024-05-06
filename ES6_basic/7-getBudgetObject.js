export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    // shorthand syntax allows for property and variable names to be identical
    income,
    gdp,
    capita
  };

  return budget;
}
