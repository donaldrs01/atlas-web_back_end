export default function signUpUser(firstName, lastName) {
  // creates Promise and passes object with specified first/last name
  return Promise.resolve({
    // use property shorthand to name properties same as variable
    firstName,
    lastName,
  });
}
