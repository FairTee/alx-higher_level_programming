#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let w = 0; w < x; w++) {
    theFunction();
  }
};
