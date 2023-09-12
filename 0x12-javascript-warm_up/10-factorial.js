#!/usr/bin/node

const argv = process.argv;

function facto (num) {
  if (num === 0) {
    return (1);
  }
  return num * facto(num - 1);
}

if (argv[2] && Number(argv[2])) {
  const num = parseInt(argv[2]);
  console.log(facto(num));
} else {
  console.log(facto(0));
}
