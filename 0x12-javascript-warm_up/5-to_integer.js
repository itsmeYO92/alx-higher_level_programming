#!/usr/bin/node
const arg_array = process.argv;

let myVar = !parseInt(arg_array[2]) ? "Not a number" : `My number: ${parseInt(arg_array[2])}`
console.log(myVar);
