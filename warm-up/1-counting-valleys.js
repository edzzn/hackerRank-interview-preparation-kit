//https://www.hackerrank.com/challenges/counting-valleys/

function countingValleys(n, s) {
  let valleysCount = 0;
  let altitude = 0;
  for (let i = 0; i < s.length; i++) {
    const element = s[i];
    if (altitude === 0 && element === "D") {
      valleysCount++;
      // console.log("new");
    }
    // console.log("TCL: countingValleys -> altitude", altitude);
    altitude = element === "D" ? altitude - 1 : altitude + 1;
  }
  return valleysCount;
}

const n = 8;
const s = "DDUUDDUDUUUD";

console.log(countingValleys(n, s));
