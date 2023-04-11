#!/usr/bin/node
const pro = process.argv.length;
console.log(pro === 2 ? 'No argument' : pro === 3 ? 'Argument found' : 'Arguments found');
