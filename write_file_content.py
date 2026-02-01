import sys
import os

if __name__ == "__main__":
    file_path = sys.argv[1]
    content = sys.stdin.read()

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Successfully wrote content to {file_path}")
