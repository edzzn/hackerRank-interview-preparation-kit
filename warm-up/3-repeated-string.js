//https://www.hackerrank.com/challenges/counting-valleys/

function repeatedString(s, n) {
  const numberOfAs = s.match(/a/gi) ? s.match(/a/gi).length : 0;
  const strLength = s.length;
  const numberOfTimes = Math.floor(n / strLength);
  const remainder = n % strLength;
  const AsInRemainder =
    remainder !== 0
      ? s.slice(0, remainder).match(/a/gi)
        ? s.slice(0, remainder).match(/a/gi).length
        : 0
      : 0;
  return numberOfTimes * numberOfAs + AsInRemainder;
}

const s = "ddda";
const n = 3;
console.log(repeatedString(s, n));
