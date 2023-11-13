#!/usr/bin/node
const argArray = process.argv;

const myVar = !parseInt(argArray[2]) ? 'Not a number' : `My number: ${parseInt(argArray[2])}`;
console.log(myVar);
