#!/usr/bin/node
const v = process.argv;
if (v.length > 3) {
  console.log(v[2] + ' is ' + v[3]);
} else if (v.length > 2) {
  console.log(v[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
