from typing import Mapping

import yaml
import io
import re

import domains
from domains import truck, wheels

a_truck = truck.Truck("SaxnioTruck", "red", ["abc", "efg"], Mapping())
a_truck.wheels = wheels.Wheels(domains.wheel.Wheel(), domains.wheel.Wheel(), domains.wheel.Wheel(),
                               domains.wheel.Wheel())

print(a_truck.name)
print("-----------")

truck_yaml = "\n".join([re.sub(r" ?!!python/.*$", "", item) for item in yaml.dump(a_truck).splitlines()])

print(truck_yaml)
stream = io.open('document.yaml', 'w')
stream.write(truck_yaml)
