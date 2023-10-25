#!/usr/bin/node

const rq = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

const st = process.argv[2];

rq(st, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
