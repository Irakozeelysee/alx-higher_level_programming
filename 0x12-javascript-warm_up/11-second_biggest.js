#!/usr/bin/node

const argv = process.argv;
let max = 0;
let max2 = 0;

if (argv.length > 3) {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num > max) {
      max = num;
    }
  }
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num !== max && num > max2) {
      max2 = num;
    }
  }
}
console.log(max2);
