import subprocess

def run_linter():
    print("Running flake8 linter...")
    result = subprocess.run(["flake8", "."], capture_output=True, text=True)
    print(result.stdout or "No linting issues found.")
    
if __name__ == "__main__":
    run_linter()