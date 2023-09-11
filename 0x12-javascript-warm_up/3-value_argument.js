#!/usr/bin/node
const argumentos = process.argv;
if (typeof argumentos[2] !== 'undefined') {
  const vivo = process.argv[2];
  console.log(vivo);
} else {
  console.log('No argument');
}
