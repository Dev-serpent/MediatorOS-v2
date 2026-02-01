#for SoCs# tasking.py
# Reads claimed tasks and executes them
import os
import json
import time
from fuser import claim_task

RESULTS = "tasks/results"
CPU_ID = "cpuA"  # match fuser.py

os.makedirs(RESULTS, exist_ok=True)

def execute_task(task_file):
    # Load the task JSON
    with open(task_file, "r") as f:
        task = json.loads(f.read())

    entry = task.get("entry")
    args = task.get("args", [])
    env = task.get("env", {})

    # Setup environment variables (optional)
    for k, v in env.items():
        try:
            setattr(__builtins__, k, v)
        except:
            pass

    result = None
    status = "done"
    try:
        # Execute the Python code file
        with open(entry) as ef:
            code = ef.read()
        local_env = {}
        exec(code, {}, local_env)
        result = local_env.get("result", None)
    except Exception as e:
        result = str(e)
        status = "error"

    # Save result
    task_id = task.get("task_id")
    out_file = "{}/task_{}_{}.json".format(RESULTS, task_id, CPU_ID)
    with open(out_file, "w") as f:
        json.dump({"task_id": task_id, "cpu": CPU_ID, "status": status, "result": result}, f)

    print("Executed task:", task_id, "Status:", status)

    # Remove the lock file
    os.remove(task_file)

# Main loop
if __name__ == "__main__":
    while True:
        task_file = claim_task()
        if task_file:
            execute_task(task_file)
        else:
            # No tasks pending, sleep briefly
            time.sleep(0.5)
