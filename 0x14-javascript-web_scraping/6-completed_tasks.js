#!/usr/bin/node

const request = require('request');
const endPoint = process.argv[2];

request.get(endPoint, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const count = {};
  body.forEach((task) => {
    if (task.completed) {
      if (!count[task.userId]) {
        count[task.userId] = 1;
      } else {
        count[task.userId] += 1;
      }
    }
  });
  console.log(count);
});
