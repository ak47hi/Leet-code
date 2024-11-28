import time

def cpu_bound_task(task_number):
    print(f"Task {task_number} started.")
    total = 0
    for i in range(10 ** 7):
        total += i * i
    print(f"Task {task_number} completed with result {total}.")

if __name__ == "__main__":
    start_time = time.perf_counter()

    for i in range(11):
        cpu_bound_task(i)

    end_time = time.perf_counter()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")