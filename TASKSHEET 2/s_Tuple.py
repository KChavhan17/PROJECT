#List v/s Tuple Decision Memo

print("                        List v/s Tuple Decision Memo                   ")
print("*"*80)
      

# Task Queue (List): Requires frequent additions, removals, and ordering changes.
task_queue = ["Task A", "Task B"]
task_queue.append(["Task C","Task D"])
task_queue.pop(0)  # Remove the first task
  # Lists are mutable, ideal for dynamic queues.
print("\nDynamic Queue:", task_queue)


# GPS Coordinates (Tuple): Data must remain constant to prevent location errors.
gps_log = (12.9716, 77.5946)  # Tuples are immutable, ensuring data integrity.
print("\nFixed GPS Coordinates:", gps_log)

try:
    gps_log[0] = 13.0827  # Attempting to modify a tuple will raise an error.
except TypeError as e:
    print(f"Error: {e}")
