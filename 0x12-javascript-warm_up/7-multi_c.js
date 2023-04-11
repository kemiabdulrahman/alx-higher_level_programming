#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let row = 0; row < num; row++) {
    console.log('C is fun');
  }
}
