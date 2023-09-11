#!/usr/bin/node
const argumentos = process.argv;

if (argumentos.length > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
