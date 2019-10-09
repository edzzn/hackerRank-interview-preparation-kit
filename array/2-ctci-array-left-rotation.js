// https://www.hackerrank.com/challenges/ctci-array-left-rotation

function rotLeft(a, d) {
  const newD = d % a.length;
  return a.slice(newD).concat(a.slice(0, newD));
}

const a = [1, 2];
const d = 3;
console.log(rotLeft(a, d));
