#!/usr/bin/node

const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
