import subprocess

def show_last_commit():
    result = subprocess.run(["git", "log", "-1"], capture_output=True, text=True)
    print("Last commit details:")
    print(result.stdout)

if __name__ == "__main__":
    show_last_commit()