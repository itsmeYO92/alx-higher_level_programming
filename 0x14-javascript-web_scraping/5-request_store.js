#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

const getBody = function (endPoint, callback) {
  request.get(endPoint, (err, res) => {
    if (err) {
      callback(err, null);
    }
    callback(null, res.body);
  });
};

getBody(url, (err, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(fileName, body, 'UTF8', err => {
    if (err) {
      console.log(err);
    }
  });
});
