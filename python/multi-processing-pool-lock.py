import multiprocessing, time

def worker(i, shared_dict, shared_list, lock):
    # print("Current count: ", shared_dict['count'])
    with lock:
        shared_dict['count'] += 0.5
        sub_func(shared_dict)
    shared_list.append(i)

def sub_func(shared_dict):
    shared_dict['count'] += 0.5

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict({'count': 0})
        shared_list = manager.list(range(0))
        lock = manager.Lock()
        worker_num = multiprocessing.cpu_count()
        tasks = []
        for i in range(100):
            tasks.append(i)
        
        with multiprocessing.Pool(processes=worker_num) as pool:
            # Pass the shared dictionary and lock to worker processes
            pool.starmap(worker, [(i, shared_dict, shared_list, lock) for i in tasks])

        # Print the final shared dictionary
        print("Processes number:", worker_num)
        print("Final shared dictionary:", dict(shared_dict))
        print("Final shared list:", shared_list)
