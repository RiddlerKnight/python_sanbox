import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH)
sys.path.append(SOURCE_PATH)

from domains.vault import Vault
def main():
  vault1 = Vault(5,5,5)
  vault2 = Vault(5,5,5)
  new_vault = vault1 + vault2
  print(new_vault)


if __name__ == "__main__":
    main()
