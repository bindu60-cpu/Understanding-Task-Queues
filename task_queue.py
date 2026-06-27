from queue import Queue

# Create a queue
task_queue = Queue()

# Add tasks
task_queue.put("Email Notification")
task_queue.put("Generate Report")
task_queue.put("Backup Database")

# Process tasks
while not task_queue.empty():
    task = task_queue.get()
    print("Processing:", task)

print("All tasks completed!")