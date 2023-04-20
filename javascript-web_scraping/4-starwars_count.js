#!/usr/bin/node

const request = require('request');

const url = `${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) console.error(error);

  const obj = JSON.parse(body);

  const movies = obj.results;

  let count = 0;

  movies.forEach((movie) => {
    movie.characters.forEach((character) => {
      if (character.includes('18')) { count++; }
    });
  });

  console.log(count);
});
