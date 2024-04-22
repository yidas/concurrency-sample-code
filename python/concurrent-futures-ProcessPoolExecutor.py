import concurrent.futures

def worker(task):
    # For monitoring CPUs
    for i in range(6000000): t = i + 1
    print(task)
    return task

if __name__ == '__main__':
    # Define tasks
    tasks = range(1000)

    # Initialize process pool executor
    # with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Asynchronously process tasks using submit
        futures = [executor.submit(worker, task) for task in tasks]

        # Get results from the async results
        final_results = [future.result() for future in concurrent.futures.as_completed(futures)]

    print("Final Results:", final_results)
