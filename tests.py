import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.write_file import write_file

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator'))

def run_tests():
    print("Test 1: write_file('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum')")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Preview:", result[:200], "...\n" if len(result) > 200 else "\n")
    if "def main():" in result:
        print("def main():")  
    print("-" * 40)

    print("Test 2: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Preview:", result[:200], "...\n" if len(result) > 200 else "\n")
    if "def _apply_operator(self, operators, values)" in result:
        print("def _apply_operator(self, operators, values)")  #
    print("-" * 40)

    print("Test 3: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Starts with 'Error:'?", result.startswith("Error:"))
    print("Message:", result)
    if "Error:" in result:
        print("Error:")  #
    print("-" * 40)

if __name__ == "__main__":
    run_tests()
