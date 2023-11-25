import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH)
sys.path.append(SOURCE_PATH)

from domains.wizard import Professor, Student, Wizard
def main():
    wizard = Professor("Albus", "Against Dart Art")
    student = Student("Harry", "Gryffindor")
    print(wizard)
    print(student)


if __name__ == "__main__":
    main()
