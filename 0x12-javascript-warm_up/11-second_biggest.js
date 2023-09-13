#!/usr/bin/node
const a = process.argv.slice(2);
gr(a);

function gr (s) {
  let i;
  let v, z;
  if (s.length === 0 || s.length === 1) {
    console.log(0);
  } else {
    for (i = 0; i < s.length - i; i++) {
      for (v = 0; v < s.length - i - 1; v++) {
        if (parseInt(s[v]) > parseInt(s[v + 1])) {
          z = s[v];
          s[v] = s[v + 1];
          s[v + 1] = z;
        }
      }
    }
    console.log(s[s.length - 2]);
  }
}
