export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      // spread syntax allows us to pass the whole employeeList into key
      // contains employee names grouped by department
      ...employeesList,
    },
    getNumberOfDepartments() {
      // method counts length of the keys array, providing us with # of departments in allEmployees obj
      return Object.keys(this.allEmployees).length;
    },
  };
}
