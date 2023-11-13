#!/usr/bin/node

function factorial (a) {
  if (!a || a === 0) {
    return 1;
  }

  return a * factorial(a - 1);
}

const a = process.argv[2];

console.log(factorial(parseInt(a)));
