#!/usr/bin/node

const fileName = process.argv[2];

const data = process.argv[3];

const fs = require('fs');

fs.writeFile(fileName, data, (error) => {
  if (error) throw error;
});
