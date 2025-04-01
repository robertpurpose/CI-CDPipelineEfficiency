
def validate_dockerfile(path="Dockerfile"):
    with open(path, "r") as file:
        content = file.read()

        checks = {
            "FROM": "Base image is defined",
            "EXPOSE": "Port is exposed",
            "CMD": "Entry point is defined",
            "ENTRYPOINT": "Entry point is defined",
        }

        for keyword, description in checks.items():
            if keyword not in content:
                print(f"❗ Missing: {description}")
            else:
                print(f"✅ Found: {description}")

if __name__ == "__main__":
    validate_dockerfile()
