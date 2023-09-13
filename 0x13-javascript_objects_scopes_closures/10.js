#!/usr/bin/node
let myarg = process.argv;
let i ;
let va = 1;
for ( i = myarg[2]; i > 1; i--) 
{
va *= i;
}
console.log(va);
