#List v/s Tuple Decision Memo

print("                        List v/s Tuple Decision Memo                   ")
print("*"*80)
      

# Task Queue (List): Requires frequent additions, removals, and ordering changes.
task_queue = ["Task A", "Task B"]
task_queue.append("Task C")  # Lists are mutable, ideal for dynamic queues.
print("\nDynamic Queue:", task_queue)


# GPS Coordinates (Tuple): Data must remain constant to prevent location errors.
gps_log = (12.9716, 77.5946)  # Tuples are immutable, ensuring data integrity.
print("\nFixed GPS Coordinates:", gps_log)
