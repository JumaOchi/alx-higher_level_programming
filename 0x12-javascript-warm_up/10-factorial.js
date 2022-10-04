#!/usr/bin/node
const myArgs = process.argv.slice(2);

function factorial(n) {
  if (n < 0) return;
  if (n === 0) return 1;
  return n * factorial(n-1);
  }

if (isNaN(myArgs[0])) {
  console.log("1");
  } else {
    console.log(factorial(parseInt(myArgs[0])));
  }
