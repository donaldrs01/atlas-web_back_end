export default function signUpUser(firstName, lastName) {
  // creates Promise and passes object with specified first/last name
  return Promise.resolve({
    firstName: firstName,
    lastName: lastName,
  });
}
