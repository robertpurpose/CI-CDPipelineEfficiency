
import subprocess
import sys

def run_tests(min_coverage=80):
    print("Running tests with coverage...")
    subprocess.run(["coverage", "run", "-m", "pytest"], check=True)
    output = subprocess.check_output(["coverage", "report"]).decode()

    lines = output.splitlines()
    total_line = [line for line in lines if "TOTAL" in line]
    if total_line:
        coverage = int(total_line[0].split()[-1].replace("%", ""))
        if coverage < min_coverage:
            print(f"🚫 Coverage {coverage}% is below minimum {min_coverage}%")
            sys.exit(1)
        else:
            print(f"✅ Coverage {coverage}% meets requirement")

if __name__ == "__main__":
    run_tests()
