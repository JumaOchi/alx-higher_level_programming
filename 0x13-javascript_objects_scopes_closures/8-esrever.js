#!/usr/bin/node

exports.esrever = function (list) {
  const listC = [];
  list.forEach(element => listC.unshift(element));
  return listC;
};
