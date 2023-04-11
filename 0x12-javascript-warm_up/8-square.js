#!/usr/bin/node
const amount = Math.floor(Number(process.argv[2]));
if (isNaN(amount)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < amount; row++) {
    let r = '';
    for (let column = 0; column < amount; column++) { r += 'X'; }
    console.log(r);
  }
}
