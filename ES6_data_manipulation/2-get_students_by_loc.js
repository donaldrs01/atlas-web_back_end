export default function getStudentsByLocation(list, city) {
  if (!Array.isArray(list)) {
    return []; // return empty array if list not an array
  }
  return list.filter((student) => student.location === city);
  // filter and return objects with passed city argument
}
