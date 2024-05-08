export default function getListStudentIds(list) {
  if (!Array.isArray(list)) {
    return []; // return empty array if list not an array
  }
  return list.map(student => student.id); // extract ID property from each student object in array
}
