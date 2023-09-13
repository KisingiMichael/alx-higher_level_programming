#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1{
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
