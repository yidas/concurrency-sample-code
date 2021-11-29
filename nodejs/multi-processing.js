const fs = require('fs');
const child_process = require('child_process');
const os = require("os")
 
const cpuNum = os.cpus().length

let promises = [];
for(var i=0; i<cpuNum; i++) {
  promises[i] = new Promise((resolve, reject) => {
    var worker_process = child_process.fork("child-process.js", [i]);

    worker_process.on('close', function (code) {
      console.log('Worker ' + i + ' close with code: ' + code);
      resolve("Worker " + i + " done")
    });
  })
}

Promise.all(promises).then((values) => {
  console.log("All Done")
});
