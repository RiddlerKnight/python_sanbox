
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH
)
sys.path.append(SOURCE_PATH)

from ex_simple_func import __main__ as init_module

def main():
    assert init_module.main() == "Works"

if __name__ == "__main__":
    main()
