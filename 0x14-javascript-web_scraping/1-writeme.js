#!/usr/bin/node
const s = require('fs');

const stk = process.argv[3];
const fl = process.argv[2];
s.writeFile(fl, stk, (err) => {
  if (err) {
    console.error(err);
  }
});
