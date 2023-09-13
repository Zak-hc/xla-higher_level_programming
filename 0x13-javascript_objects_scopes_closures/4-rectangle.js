#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return ('Rectangle{}');
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    const v = 'X'.repeat(this.width);
    for (i = 0; i < this.height; i++) {
      console.log(v);
    }
  }

  rotate () {
    const save = this.width;
    this.width = this.height;
    this.height = save;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
