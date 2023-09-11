#!/usr/bin/node
const argumentos = process.argv;

if ( argumentos.length > 3) {
  console.log('Arguments found');
} else if (argumentos.length > 2) {
  console.log('Argument found');
} else {
  console.log('no argument');
}
