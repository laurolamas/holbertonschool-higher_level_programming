#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || isNaN(w) || isNaN(h))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      if (i !== this.height - 1) {
        console.log();
      }
    }
    console.log();
  }
}

module.exports = Rectangle;
