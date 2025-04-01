
import subprocess

def run_linters():
    print("Running Black formatter...")
    subprocess.run(["black", "."], check=True)

    print("Running Flake8 linter...")
    subprocess.run(["flake8", "."], check=True)

if __name__ == "__main__":
    run_linters()
