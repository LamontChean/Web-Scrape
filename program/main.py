# 1. What is parallel programming
# a practice of running multiple computations at the same time, 
# typically accross different processors or cores

# 2. Why use parallel programming
# working with large data sets
# performing CPU-heavy tasks
# speeding up tasks that can be broken down into smaller independent parts

# 3. Concurrency vs Parallelism
# concurrency: dealing with multiple tasks at once, but not necessarily at 
# the same time
# parallelism: doing multiple tasks at the same time, using multiple CPU cores

import time 
import random
import concurrent.futures

def task(n):
    time.sleep(random.uniform(0.5, 1.5))
    if random.random() < 0.2:
        raise ValueError(f"Task failed for {n}")
    return n ** 2

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(task, i): i for i in range(5)}

        for future in concurrent.futures.as_completed(futures):
            task_id = futures[future]
            try:
                print(f"Result {task_id}: {future.result()}")
            except Exception as e: 
                print(f"Result {task_id}: failed")

if __name__ == "__main__":
    main()
