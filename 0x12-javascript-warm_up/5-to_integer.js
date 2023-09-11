#!/usr/bin/node
const v = process.argv;
if (!isNaN(v[2])) {
  console.log('My number: ' + v[2]);
} else {
  console.log('Not a number');
}
