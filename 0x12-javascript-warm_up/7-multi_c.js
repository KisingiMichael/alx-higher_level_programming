#!/usr/bin/node
const loveC = 'C is fun';
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(loveC);
  }
}
