#!/usr/bin/node

const dict = require('./101-data').dict;

const res = {};
for (const key in dict) {
  if (res[dict[key]] === undefined) {
    res[dict[key]] = [key];
  } else {
    res[dict[key]].push(key);
  }
}

console.log(res);
