export default function createEmployeesObject(departmentName, employees) {
  const employeesObject = {
    [departmentName]: employees // computed property name allows for dynamic creation of object key
  };

  return employeesObject;
}
