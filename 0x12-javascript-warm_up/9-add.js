#!/usr/bin/node
function add (x, y) {
  const q = x + y;
  console.log(q);
}
add(Number(process.argv[2]), Number(process.argv[3]));
