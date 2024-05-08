export default function appendToEachArrayValue(array, appendString) {
  const newArraw = [];
  for (const element of array) {
    newArraw.push(appendString + element);
  }
  return newArraw;
}
