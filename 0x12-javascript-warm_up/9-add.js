#!/usr/bin/env node

function add(a, b) {
	  return parseInt(a) + parseInt(b);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!isNaN(arg1) && !isNaN(arg2)) {
	  console.log(add(arg1, arg2));
} else {
	  console.log('NaN');
}
