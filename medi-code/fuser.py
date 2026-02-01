#for mediatorOS
# fuser.py
# Claims tasks atomically for a single CPU
import os

PENDING = "tasks/pending"
RUNNING = "tasks/running"

CPU_ID = "cpuA"  # change for each node/phone

def claim_task():
    os.makedirs(RUNNING, exist_ok=True)

    for fname in os.listdir(PENDING):
        if not fname.endswith(".json"):
            continue

        src = "{}/{}".format(PENDING, fname)
        dst = "{}/{}.{}.lock".format(RUNNING, fname, CPU_ID)

        try:
            os.rename(src, dst)  # atomic on most filesystems
            print("Claimed task:", dst)
            return dst
        except OSError:
            # another CPU claimed it
            continue

    return None

# Test runner
if __name__ == "__main__":
    task = claim_task()
    if task:
        print("Task ready:", task)
    else:
        print("No tasks pending")
