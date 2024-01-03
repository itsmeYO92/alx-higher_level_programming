#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
fs.readFile(fileName, 'UTF8', function (err, data) {
  if (err) {
    throw err;
  }
  console.log(data);
});
