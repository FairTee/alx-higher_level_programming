#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const a = Number(process.argv[2]);
  let v = 0;
  while (v < a) {
    console.log('X'.repeat(a));
    v++;
  }
}
