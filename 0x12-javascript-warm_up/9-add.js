#!/usr/bin/node

function add (a, b) {
  if (!parseInt(a) || !parseInt(b)) {
    return NaN;
  }

  return parseInt(a) + parseInt(b);
}

const a = process.argv[2];
const b = process.argv[3];

console.log(add(a, b));
