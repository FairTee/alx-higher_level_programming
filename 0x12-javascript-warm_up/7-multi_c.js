#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const a = Number(process.argv[2]);
  let v = 0;
  while (v < a) {
    console.log('C is fun');
    v++;
  }
}
