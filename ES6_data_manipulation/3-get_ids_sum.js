export default function getStudentIdsSum(list) {
  if (!Array.isArray(list)) {
    return []; // return empty array if list not an array
  }
  return list.reduce((sum, student) => sum + student.id, 0);
  // sum holds current value and initial value set to 0
}
