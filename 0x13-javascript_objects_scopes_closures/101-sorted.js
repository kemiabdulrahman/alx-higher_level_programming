#!/usr/bin/node
const dict = require('./101-data').dict;
const totallist = Object.entries(dict);
const values = Object.values(dict);
const uniqueValues = [...new Set(values)];
const Ndict = {};
for (const j in uniqueValues) {
  const list = [];
  for (const k in uniqueValues) {
    if (totallist[k][1] === uniqueValues[j]) {
      list.unshift(totallist[k][0]);
    }
  }
  Ndict[uniqueValues[j]] = list;
}
console.log(Ndict);
