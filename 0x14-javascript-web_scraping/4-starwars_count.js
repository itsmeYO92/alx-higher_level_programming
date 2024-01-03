#!/usr/bin/node

const request = require('request');
const id = '18';
const endPoint = process.argv[2];
let count = 0;

request.get(endPoint, (err, res) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(res.body);
  const results = data.results;
  results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(id)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
