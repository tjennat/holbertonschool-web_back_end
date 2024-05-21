export default function getStudentIdsSum(array) {
  return array.reduce((acc, student) => acc + student.id, 0);
}
