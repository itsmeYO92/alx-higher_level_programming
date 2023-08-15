#!/usr/bin/node

let count = 0;

exports.logMe = function count (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};

