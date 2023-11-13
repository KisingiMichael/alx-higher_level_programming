#!/usr/bin/node
const sqrSize = process.argv[2];
if (isNaN(sqrSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqrSize; i++) {
    console.log('X'.repeat(sqrSize));
  }
}
