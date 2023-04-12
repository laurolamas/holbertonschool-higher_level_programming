#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const args = process.argv;

const a = parseInt(args[2]);
const b = parseInt(args[3]);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
