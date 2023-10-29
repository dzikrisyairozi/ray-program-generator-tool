import ray
import time

ray.init()

# Define a Ray remote function that simulates a time-consuming task
@ray.remote
def slow_function(i):
    time.sleep(1)
    return i

# Execute multiple tasks in parallel
start_time = time.time()
results = ray.get([slow_function.remote(i) for i in range(4)])
end_time = time.time()

print(f"Results: {results}")
print(f"Execution time: {end_time - start_time} seconds")
