#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

const txt1 = fs.readFileSync(argv[2], 'utf8');
const txt2 = fs.readFileSync(argv[3], 'utf8');
fs.writeFileSync(argv[4], txt1 + txt2);
