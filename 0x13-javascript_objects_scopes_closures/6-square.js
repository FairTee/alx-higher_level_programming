#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    // Print the square using the specified character or 'X' by default
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
