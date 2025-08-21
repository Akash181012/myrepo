# main.py
import datetime

def greet(name: str):
    print(f"Hello, {name}! Welcome to Jenkins + GitLab CI/CD 🚀")
    print(f"Current build time: {datetime.datetime.now()}")

if __name__ == "__main__":
    greet("Akash")   # change name as needed
