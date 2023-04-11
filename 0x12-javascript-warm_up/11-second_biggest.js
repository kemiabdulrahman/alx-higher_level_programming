#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argum = process.argv.map(Number).slice(2, process.argv.length).sort((b, c) => b - c);
  console.log(argum[argum.length - 2]);
}
