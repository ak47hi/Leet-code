import multiprocessing
import time

def cpu_bound_task(task_number):
    print(f"Process {task_number} started.")
    # Simulate a CPU-bound task (e.g., compute-intensive calculation)
    total = 0
    for i in range(10 ** 7):
        total += i * i
    print(f"Process {task_number} completed with result {total}.")

if __name__ == "__main__":
    start_time = time.perf_counter()

    processes = []
    num_processes = 11  # Number of processes to match the number of cores

    for i in range(num_processes):
        p = multiprocessing.Process(target=cpu_bound_task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.perf_counter()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")