#!/usr/bin/node
const v = process.argv;
if (!isNaN(v[2])) {
  temporino(v);
} else {
  console.log('Missing size');
}

function temporino (a) {
  let i;
  let piw;
  let b;
  for (i = 0; i < a[2]; i++) {
    piw = '';
    for (b = 0; b < a[2]; b++) { piw += 'X'; }
    console.log(piw);
  }
}
