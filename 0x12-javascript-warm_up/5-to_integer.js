#!/usr/bin/node

const argv = process.argv;

if (argv[2] && Number(argv[2])) {
  console.log(`My number: ${parseInt(argv[2])}`);
} else {
  console.log('Not a number');
}
