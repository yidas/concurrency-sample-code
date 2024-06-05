const { parentPort, workerData } = require('worker_threads');

// Log the worker's unique ID and process ID
console.log(`Worker thread ${workerData.id} with process ID ${process.pid} is running`);

// For monitoring usage of CPU cores
for (let i = 0; i < 4000000000; i++) { sum = 1 + i; }
result = 'Result-' + workerData.id

// Send the result back to the main thread
parentPort.postMessage({ id: workerData.id, result });
