export default function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  const id = array.map((student) => student.id);
  return id;
}
