#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (isNaN(myArgs[0])) {
  console.log('Missing size');
  } else {
    let x = parseInt(myArgs[0]);
    for (let i = 0; i < x; i++) {
      for (let j = 0; j < x; j++) {
        process.stdout.write("X");
	}
      console.log("");
      }
  }
