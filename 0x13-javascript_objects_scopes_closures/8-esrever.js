#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let y = 0;
  const listta = [];
  for (i = list.length - 1; i >= 0; i--) {
    listta[y] = list[i];
    y++;
  }
  return listta;
};
