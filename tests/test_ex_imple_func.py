
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH
)
sys.path.append(SOURCE_PATH)

from ex_simple_func import __main__ as init_module

def test_ex_simple_func():
    assert init_module.main() == "Works"
