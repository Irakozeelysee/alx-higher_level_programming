#!/usr/bin/node

const argv = process.argv;

if (argv[2] && Number(argv[2])) {
  let x = parseInt(argv[2]);
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
