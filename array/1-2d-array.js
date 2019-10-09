function hourglassSum(arr) {
  let maxSum = -Infinity;

  for (let i = 2; i < 6; i++) {
    console.log(i);

    for (let j = 0; j < 4; j++) {
      console.log("   ", j);
      console.log(arr[i][j]);
      const sum =
        arr[i][j] +
        arr[i][j + 1] +
        arr[i][j + 2] +
        arr[i - 1][j + 1] +
        arr[i - 2][j] +
        arr[i - 2][j + 1] +
        arr[i - 2][j + 2];
      maxSum = sum > maxSum ? sum : maxSum;
    }
  }

  return maxSum;
}

const arr = [
  [1, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0],
  [0, 0, 2, 4, 4, 0],
  [0, 0, 0, 2, 0, 0],
  [0, 0, 1, 2, 4, 0]
];

console.log(hourglassSum(arr));
