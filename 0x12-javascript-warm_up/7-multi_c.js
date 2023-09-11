#!/usr/bin/node
let v = process.argv;
if(!isNaN(v[2]))
{
temporino(v);
}
else
{
console.log('Missing number of occurrences');
}

function temporino(a)
{
let i;
for(i = 0; i < a[2]; i++)
{
console.log('C is fun');
}
}

