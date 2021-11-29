import multiprocessing as mp

def work(queue, num):
    # Check multiprocessing Queue
    while queue.empty() == False:
        # Get data from queue
        task = queue.get()

        # For monitoring CPUs
        for i in range(6000000): t = i + 1

        print("Worker %d: %s" % (num, task))

# Main process
if __name__ == '__main__':
    # Config
    workerNum = mp.cpu_count();
    print("Number of workers (CPU cores) to start multi-processing: {}".format(workerNum))

    queue = mp.Queue()

    # Put tasks into the queue
    for i in range(100):
        queue.put("Data %d" % i)

    worker = {}
    for i in range(workerNum):
        worker[i] = mp.Process(target=work, args = (queue, i))
        worker[i].start()

    # Wait for all workers to complete
    for i in worker:
        worker[i].join()

    print("Done.")