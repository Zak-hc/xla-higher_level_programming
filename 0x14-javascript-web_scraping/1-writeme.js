#!/usr/bin/node
const fs = require('fs');
const stk = process.argv[3];
const fl = process.argv[2];
fs.writeFile(fl, stk, (err) => {
	if (err) {
		console.error(err);
	}
	});
