#!/usr/bin/node

exports.esrever = function (list) {
  const newArrList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newArrList.push(list[i]);
  }
  return (newArrList);
};
