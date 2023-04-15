#!/usr/bin/node

exports.esrever = function (list) {
  const revList = new Array(list.length);
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    revList[j] = list[i];
    j++;
  }
  return (revList);
};
