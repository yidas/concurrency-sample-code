import concurrent.futures
import time, random

def worker(task):
    # For monitoring I/O
    time.sleep(random.uniform(0.1, 5))
    print(task)
    return task

def main():
    # Define tasks
    tasks = range(1000)

    worker_num = len(tasks)

    # Initialize process pool executor
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker_num) as executor:
        # Asynchronously process tasks using submit
        futures = [executor.submit(worker, task) for task in tasks]

        # Get results from the async results
        final_results = [future.result() for future in concurrent.futures.as_completed(futures)]

    print("Final Results:", final_results)

main()
