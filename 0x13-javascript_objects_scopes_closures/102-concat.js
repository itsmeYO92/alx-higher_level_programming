#!/usr/bin/node

const argv = process.argv;
const file1Path = `./${argv[2]}`;
const file2Path = `./${argv[3]}`;
const savingPath = `./${argv[4]}`;

const fileReader = require('fs');

fileReader.readFile(file1Path, 'utf8', (err, data) => {
  if (err) {
    return;
  }

  fileReader.writeFileSync(savingPath, data);
});

fileReader.readFile(file2Path, 'utf8', (err, data) => {
  if (err) {
    return;
  }

  fileReader.appendFileSync(savingPath, data);
});
