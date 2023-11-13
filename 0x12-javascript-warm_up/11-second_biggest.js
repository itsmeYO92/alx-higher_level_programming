#!/usr/bin/node
const argArray = process.argv;

if (argArray.length < 4) {
  console.log(0);
} else {
  const sortedArray = argArray.map(Number).slice(2).sort((a, b) => a - b);
  console.log(sortedArray[sortedArray.length - 2]);
}
