// https://www.hackerrank.com/challenges/ctci-array-left-rotation

"use strict";

const fs = require("fs");

// Complete the rotLeft function below.
function rotLeft(a, d) {
  console.log("TCL: rotLeft -> d", d);
  const newD = d % a.length;
  return a.slice(newD).concat(a.slice(0, newD));
}

function main() {
  const file = fs.readFileSync("./2-testcase.txt", "utf8");
  console.log("TCL: main -> file ", file.split("\n")[1].split(" "));
  const a = file.split("\n")[1].split(" ");
  const d = file.split("\n")[0].split(" ")[1];
  console.log(rotLeft(a, d));
}

main();
