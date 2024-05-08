export default function updateStudentGradeByCity(list, city, newGrades) {
  const filteredStudents = list.filter((student) => student.location === city);
  // Filter students by given city
  const updatedStudents = filteredStudents.map((student) => {
    const newGrade = newGrades.find((grade) => grade.studentId === student.id);
    if (newGrade) {
      return { ...student, grade: newGrade.grade }
      // Spread syntax to create new student obj with newGrade
    }
    return { ...student, grade: 'N/A' }; // Set grade to 'N/A' if grade empty
  });

  return updatedStudents;
}
