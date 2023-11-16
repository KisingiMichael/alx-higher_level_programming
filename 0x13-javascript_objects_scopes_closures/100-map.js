#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const myList = list.map((num, elem) => num * elem);
console.log(myList);
