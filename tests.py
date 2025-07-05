import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.run_python_file import run_python_file



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator'))

def run_tests():
    print("Test 1: run_python_file('calculator', 'main.py')")
    result = run_python_file("calculator", "main.py")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Preview:", result[:200], "...\n" if len(result) > 200 else "\n")
    print("-" * 40)

    print("Test 2: run_python_file('calculator', 'tests.py')")
    result = run_python_file("calculator", "tests.py")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Preview:", result[:200], "...\n" if len(result) > 200 else "\n")
    print("-" * 40)

    print("Test 3: run_python_file('calculator', '../main.py')")
    result = run_python_file("calculator", "../main.py")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Message:", result)
    print("-" * 40)

    print("Test 4: run_python_file('calculator', 'nonexistent.py')")
    result = run_python_file("calculator", "nonexistent.py")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Message:", result)
    print("-" * 40)

if __name__ == "__main__":
    run_tests()
