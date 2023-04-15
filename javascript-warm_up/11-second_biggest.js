#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let max = parseInt(args[0]);
  let sndMax = parseInt(args[1]);
  let x;

  if (sndMax > max) {
    [max, sndMax] = [sndMax, max];
  }

  for (let i = 2; i < args.length; i++) {
    x = parseInt(args[i]);

    if (x > max) {
      sndMax = max;
      max = x;
    } else if (x > sndMax && x !== max) {
      sndMax = x;
    }
  }

  console.log(sndMax);
}
