export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  let clean = '';

  set.forEach((element) => {
    if (element.startsWith(startString)) {
      clean += `${element.substring(startString.length)}-`;
    }
  });

  clean = clean.slice(0, -1);

  return clean;
}
