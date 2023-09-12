#!/usr/bin/node

const argv = process.argv;

if ((argv[2] && Number(argv[2])) && (argv[3] && Number(argv[3]))) {
  const res = parseInt(argv[2]) + parseInt(argv[3]);
  console.log(`${res}`);
} else {
  console.log('NaN');
}
