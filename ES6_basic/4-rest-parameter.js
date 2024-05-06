// Rest parameter allows for an indefinite number of args
export default function returnHowManyArguments(...rest) {
  return rest.length;
}
