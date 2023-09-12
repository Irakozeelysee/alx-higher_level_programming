#!/usr/bin/env node

function factorial(n) {
	if (isNaN(n)) {
		return 1;
	}
	n = parseInt(n);
	if (n === 0 || n === 1) {
		return 1;
	} else if (n < 0) {
		return Infinity;
	} else {
		return n * factorial(n - 1);
	}
}
const arg = process.argv[2];

console.log(factorial(arg));
