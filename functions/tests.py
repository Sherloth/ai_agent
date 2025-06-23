import os
from get_files_info import get_files_info

# calculate absolute path to calculator folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator'))

def run_tests():
    print("Test 1: get_files_info(BASE_DIR, '.')")
    result = get_files_info(BASE_DIR, '.')
    print(result)
    print("-" * 40)

    print("Test 2: get_files_info(BASE_DIR, 'pkg')")
    result = get_files_info(BASE_DIR, 'pkg')
    print(result)
    print("-" * 40)

    print("Test 3: get_files_info(BASE_DIR, '/bin')")
    result = get_files_info(BASE_DIR, '/bin')
    print(result)
    print("-" * 40)

    print("Test 4: get_files_info(BASE_DIR, '../')")
    result = get_files_info(BASE_DIR, '../')
    print(result)
    print("-" * 40)

if __name__ == "__main__":
    run_tests()
