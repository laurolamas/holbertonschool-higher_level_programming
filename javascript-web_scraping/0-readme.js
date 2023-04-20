#!/usr/bin/node

const fileName = process.argv[2];

const fs = require('fs');

fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
