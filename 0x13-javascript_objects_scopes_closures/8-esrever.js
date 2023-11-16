#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = [];
  for (let x = list.length - 1; x >= 0; x--) {
    newArray.push(list[x]);
  }
  return (newArray);
};
