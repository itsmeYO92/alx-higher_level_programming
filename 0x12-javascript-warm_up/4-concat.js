#!/usr/bin/node
const arg_array = process.argv;

let myVar = arg_array[2] ? arg_array[2] : "undefined";
myVar += " is " + (arg_array[3] ? arg_array[3] : "undefined");
console.log(myVar)
