#!/usr/bin/node

function formatNumber(num) {
  if (num === Infinity) {
    return 'Infinity';
  } else if (num >= 1e100) {
    return num.toString();
  } else {
    return num.toString();
  }
}

function factorial(n) {
  if (n < 0) {
    return 'Factorial is undefined for negative numbers';
  } else if (n === 0) {
    return 1n; // Factorial of 0 is 1
  } else {
    let result = 1n;
    for (let i = 1n; i <= n; i++) {
      result *= i;
    }
    return result;
  }
}

const input = process.argv[2];
const num = BigInt(input);

const result = factorial(num);

console.log(formatNumber(result));

