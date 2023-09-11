#!/usr/bin/node
const a = process.argv;
if (!isNaN(a[2])) {
  add(Number(a[2]));
} else {
  console.log('1');
}
function add (a) {
  console.log(a * a);
}
