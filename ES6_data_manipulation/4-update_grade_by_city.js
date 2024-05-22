export default function updateStudentGradeByCity(array, city, newGrades) {
  if (!Array.isArray(array)) {
    return [];
  }
  const newArray = array
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

      return {
        ...student,
        grade: matchingGrade ? matchingGrade.grade : 'N/A',
      };
    });

  return newArray;
}
