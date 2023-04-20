#!/usr/bin/node

const movieid = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

const request = require('request');

request(url, (error, response, body) => {
  if (error) console.error(error);

  const obj = JSON.parse(body);

  console.log(obj.title);
});
