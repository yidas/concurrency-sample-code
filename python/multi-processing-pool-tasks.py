from multiprocessing import Pool, cpu_count
import os, time, random

def worker(seq):
    # For monitoring CPUs
    for i in range(600000): t = i + 1
    # time.sleep(random.randrange(3, 4))
    print(seq)
    return seq


if __name__ == '__main__':
     # Define tasks
    tasks = range(1000)

    # Set processes number
    cpu_count = os.cpu_count()
    pool = Pool(cpu_count)
    print("Pool processor number: ", cpu_count)

    # Pool - apply_async method
    results = [pool.apply_async(worker, args=(task,)) for task in tasks]

    # Get results from the async results
    final_results = [result.get() for result in results]

    # Close the pool (optional, but recommended)
    pool.close()
    pool.join()

    print("Final Results:", final_results)
