#!/usr/bin/node
const parentSquare = require('./5-square');
class Square extends parentSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      let ii;
      const ri = 'X'.repeat(this.width);
      for (ii = 0; ii < this.height; ii++) { console.log(ri); }
    } else {
      let ii;
      const ri = c.repeat(this.width);
      for (ii = 0; ii < this.height; ii++) {
        console.log(ri);
      }
    }
  }
}
module.exports = Square;
