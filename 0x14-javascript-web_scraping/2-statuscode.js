#!/usr/bin/node
const rq = require('request');
const st = process.argv[2];

rq(st, (error, response) => {
	if (error) {
		console.error(error);
	} else {
		console.log(`code: ${response.statusCode}`);
	}
	});
