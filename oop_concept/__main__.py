import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH)
sys.path.append(SOURCE_PATH)

from domains.truck import Truck
from domains.wheel import Wheel
from domains.wheels import Wheels

def main():
    print("OK")
    truck_obj = Truck("MyTruck", "Red", ["vvv", "ggg"], {"owner":"korn"}, 
                      Wheels(
                          Wheel(),
                          Wheel(),
                          Wheel(),
                          Wheel()
                          ))
    
    print(f"What The obj: {truck_obj}")
    print(f"Truck Name: {truck_obj.name}")
    print(f"Wheel 1: {truck_obj.wheels.fl.model}")


if __name__ == "__main__":
    main()
