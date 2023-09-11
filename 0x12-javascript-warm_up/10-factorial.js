#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative numbers is 1
  } else if (n === 0) {
    return 1; // Factorial of 0 is 1
  } else {
    let result = 1n; // Initialize result as a BigInt
    for (let i = 1; i <= n; i++) {
      result *= BigInt(i);
    }
    return result;
  }
}

const input = process.argv[2];
const num = parseInt(input, 10);

const result = factorial(num);

console.log(result.toString());
