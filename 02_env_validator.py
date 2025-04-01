import os

def validate_env_vars(required_vars):
    missing = [var for var in required_vars if os.getenv(var) is None]
    if missing:
        print("Missing environment variables:", missing)
        return False
    print("All required environment variables are set.")
    return True

if __name__ == "__main__":
    validate_env_vars(["DATABASE_URL", "SECRET_KEY", "API_TOKEN"])