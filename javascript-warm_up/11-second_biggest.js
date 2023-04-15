#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  let max = parseInt(args[2]);
  let sndMax = parseInt(args[2]);
  let x = parseInt(args[2]);

  for (let i = 2; i < args.length; i++) {
    x = parseInt(args[i]);
    console.log(`x = ${x}`);
    if (x > sndMax && x < max) {
      sndMax = x;
    } else if (x > max) {
      max = x;
    }
  }

  console.log(sndMax);
}
