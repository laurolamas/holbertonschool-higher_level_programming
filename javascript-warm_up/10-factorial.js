#!/usr/bin/node

function factorial (x) {
  if (isNaN(x) || x === 1) {
    return 1;
  }
  return (x * factorial(x - 1));
}

const args = process.argv;

const x = parseInt(args[2]);

console.log(factorial(x));
