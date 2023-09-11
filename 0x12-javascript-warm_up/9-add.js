#!/usr/bin/node
const a = process.argv;
if (!isNaN(a[2]) && !isNaN(a[3])) {
  add(Number(a[2]), Number(a[3]));
} else {
  console.log('NaN');
}
function add (a, b) {
  console.log(a + b);
}
