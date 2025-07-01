import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.get_file_content import get_file_content



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator'))

def run_tests():
    print("Test 1: get_file_content('calculator', 'main.py')")
    result = get_file_content("calculator", "main.py")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Preview:", result[:200], "...\n" if len(result) > 200 else "\n")
    print("-" * 40)

    print("Test 2: get_file_content('calculator', 'pkg/calculator.py')")
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Preview:", result[:200], "...\n" if len(result) > 200 else "\n")
    print("-" * 40)

    print("Test 3: get_file_content('calculator', '/bin/cat') (should return error)")
    result = get_file_content("calculator", "/bin/cat")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Message:", result)
    print("-" * 40)

if __name__ == "__main__":
    run_tests()
