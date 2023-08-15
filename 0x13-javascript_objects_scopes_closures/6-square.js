#!/usr/bin/node
const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;