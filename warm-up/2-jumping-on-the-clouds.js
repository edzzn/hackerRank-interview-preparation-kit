// https://www.hackerrank.com/challenges/jumping-on-the-clouds
function jumpingOnClouds(c) {
  let jumpCount = 0;
  for (let i = 0; i < c.length - 1; i++) {
    console.log(i + 2, c[i + 2]);
    if (c[i + 2] === 0) {
      i++;
    }
    jumpCount++;
  }
  return jumpCount;
}

// 0 = SAFE
const c = [0, 0, 1, 0, 0, 1, 0];

console.log(jumpingOnClouds(c));
