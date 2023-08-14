#!/usr/bin/node
const arg_array = process.argv;

if (arg_array.length < 4) {
  console.log(0);
} else {
  let sorted_array = arg_array.slice(2).sort();
  console.log(sorted_array[sorted_array.length - 2])
}
