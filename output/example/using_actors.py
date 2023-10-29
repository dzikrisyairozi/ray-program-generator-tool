import ray

ray.init()

# Define a Ray actor class
@ray.remote
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

# Create an actor from the Counter class
counter = Counter.remote()

# Interact with the actor
ray.get(counter.increment.remote())
ray.get(counter.increment.remote())

# Retrieve the final value
final_value = ray.get(counter.increment.remote())
print(f"Final value of counter: {final_value}")
