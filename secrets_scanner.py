
import re
import os

def scan_secrets(directory="."):
    secret_patterns = [
        r'AKIA[0-9A-Z]{16}',
        r'(?i)apikey\s*[:=]\s*[\'\"].{32,}[\'\"']',
        r'(?i)password\s*[:=]\s*[\'\"].+?[\'\"']',
    ]

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".py", ".env", ".yml", ".json")):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for pattern in secret_patterns:
                        if re.search(pattern, content):
                            print(f"🔒 Potential secret found in {path}")
                            break

if __name__ == "__main__":
    scan_secrets()
