#!/usr/bin/node
const x = process.argv[2];

const i = parseInt(x);
if (!i) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
