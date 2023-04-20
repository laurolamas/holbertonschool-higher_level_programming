#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.error(error);

  fs.writeFile(fileName, body, (error) => {
    if (error) throw error;
  });
});
