const {
    Worker,
    isMainThread,
    parentPort
} = require('worker_threads');

if (isMainThread) {
    const numWorkers = 4; // Adjust the number of workers
    const results = [];
    let completedWorkers = 0;
    // This code is executed in the main thread
    for (let i = 0; i < numWorkers; i++) { // Adjust the number of workers
        const worker = new Worker('./child-thread.js', {
            workerData: {
                id: i
            }
        });
        worker.on('message', handleWorkerResult);
    }

    function handleWorkerResult(data) {
        results.push(data);
        completedWorkers++;
        if (completedWorkers === numWorkers) {
            console.log('All workers completed their tasks');
            console.log('Results:', results);
        }
    }
} else {
    console.log(`Worker thread is running`);
}