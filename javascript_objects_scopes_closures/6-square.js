#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      if (i !== this.height - 1) {
        console.log();
      }
    }
    console.log();
  }
}

module.exports = Square;
