#!/usr/bin/node
const arg = process.argv[2];
let x = parseInt(arg);
if (!x) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log("X".repeat(x));
  }
}
