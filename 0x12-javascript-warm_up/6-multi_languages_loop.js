#!/usr/bin/node
const vi = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
printo(vi);

function printo (a) {
  let i;
  for (i = 0; i < a.length; i++) {
    console.log(a[i]);
  }
}
