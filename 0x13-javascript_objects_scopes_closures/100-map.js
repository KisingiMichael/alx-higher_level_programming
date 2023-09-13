#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((value, elem) => value * elem);
console.log(newList);
