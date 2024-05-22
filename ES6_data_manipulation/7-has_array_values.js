export default function hasValuesFromArray(dataSet, array) {
  return array.every((element) => dataSet.has(element));
}
