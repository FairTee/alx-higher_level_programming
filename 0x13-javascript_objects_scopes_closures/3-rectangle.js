#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not a positive integer
      Object.create(null);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let q = '';
      for (let j = 0; j < this.width; j++) {
        q += 'X';
      }
      console.log(q);
    }
  }
}

module.exports = Rectangle;
