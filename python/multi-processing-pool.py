from multiprocessing import Process, Pool, cpu_count
import os, time, random

def main_map(seq):
    # For monitoring CPUs
    for i in range(6000000): t = i + 1
    # time.sleep(random.randrange(3, 4))
    return seq


if __name__ == '__main__':
    inputs = []
    for i in range(10):
        inputs.append(i)

    # Set processes number
    cpu_count = os.cpu_count()
    pool = Pool(cpu_count)
    print("Pool processor number: ", cpu_count)

    # Execute multi-processing
    pool_outputs = pool.map(main_map, inputs)

    print(pool_outputs)