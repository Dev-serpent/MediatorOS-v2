#for MediatorOS
# dumpgen.py
# Generates tasks and puts them into tasks/pending/
import os
import json
import time

try:
    import random  # MicroPython has this
except ImportError:
    print("No random module found! Using fallback.")
    random = None

TASK_DIR = "tasks/pending"

def gen_task_id():
    if random:
        # simple pseudo-random hex ID
        return "{:08x}".format(random.getrandbits(32))
    else:
        # fallback to timestamp
        return str(int(time.time() * 1000))

def dumpgen(entry, args=None, env=None):
    os.makedirs(TASK_DIR, exist_ok=True)

    task_id = gen_task_id()
    task = {
        "task_id": task_id,
        "type": "python",
        "entry": entry,
        "args": args or [],
        "env": env or {},
        "created": time.time()
    }

    path = "{}/task_{}.json".format(TASK_DIR, task_id)
    with open(path, "w") as f:
        f.write(json.dumps(task))

    print("Created task:", task_id)
    return task_id

# Example usage
if __name__ == "__main__":
    dumpgen("kernel.py", [10, 20], {"MODE": "FAST"})
