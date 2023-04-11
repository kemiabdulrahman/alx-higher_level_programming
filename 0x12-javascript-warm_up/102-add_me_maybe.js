#!/usr/bin/node
exports.addOn = function (number, theFunction) {
  theFunction(++number);
};
