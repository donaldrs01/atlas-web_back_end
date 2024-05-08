export default function getStudentIdsSum(list) {
  if (!Array.isArray(list)) {
    return []; // return empty array if list not an array
  }
  return list.reduce((sum, student) => sum + student.id);
  // sum holds current value
}
