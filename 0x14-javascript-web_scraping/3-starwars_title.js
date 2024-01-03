#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(endPoint, (err, res) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(res.body);
  console.log(data.title);
});
