#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let numberOfOccurrence = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      numberOfOccurrence++;
    }
  }
  return numberOfOccurrence;
};
