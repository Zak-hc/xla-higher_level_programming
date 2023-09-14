#!/usr/bin/node
let clc = 0;
exports.logMe = function (item) {
  console.log(clc + ': ' + item);
  clc += 1;
};
