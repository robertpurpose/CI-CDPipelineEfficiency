
import re

def bump_version(file="__init__.py"):
    with open(file, "r+") as f:
        content = f.read()
        match = re.search(r'__version__ = "(\d+)\.(\d+)\.(\d+)"', content)
        if match:
            major, minor, patch = map(int, match.groups())
            new_version = f'{major}.{minor}.{patch + 1}'
            new_content = re.sub(r'__version__ = ".*"', f'__version__ = "{new_version}"', content)
            f.seek(0)
            f.write(new_content)
            f.truncate()
            print(f"Version bumped to {new_version}")

if __name__ == "__main__":
    bump_version()
