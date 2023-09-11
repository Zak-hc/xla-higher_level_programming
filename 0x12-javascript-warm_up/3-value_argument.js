#!/usr/bin/node
const argumentos = process.argv;
if (argumentos.length > 2) {
  const vivo = process.argv[2];
  console.log(vivo);
} else {
  console.log('No argument');
}
