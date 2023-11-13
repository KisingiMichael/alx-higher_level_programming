#!/usr/bin/node
function fact (n) {
  return n === 0 || isNaN(n) ? 1 : n * fact(n - 1);
}
console.log(fact(Number(process.argv[2])));
