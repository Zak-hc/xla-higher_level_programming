#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const v = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(v);
    }
  }
}
module.exports = Rectangle;
