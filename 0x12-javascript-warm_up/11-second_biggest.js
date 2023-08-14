#!/usr/bin/node
const arg_array = process.argv;

if (arg_array.length < 4) {
  console.log(0);
} else {
  let sorted_array = arg_array.map(Number).slice(2).sort((a, b) => a - b);
  console.log(sorted_array[sorted_array.length - 2])
}
