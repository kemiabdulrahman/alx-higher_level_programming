#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let h = 0; h < this.height; h++) {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
