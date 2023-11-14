#!/usr/bin/node
exports.addMeMaybe = function (n, theFunction) {
  theFunction(++n);
};
