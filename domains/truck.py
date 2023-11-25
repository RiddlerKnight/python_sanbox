from typing import Mapping
from domains.wheels import Wheels


class Truck:

    def __init__(self, name: str, color: str, additional: list[str], profile: Mapping[str, str],
                 wheels: Wheels = None):
        self.profile = profile
        self.additional = additional
        self.name = name
        self.color = color
        self.wheels = wheels

    '''
    if you didn't specify this method, you will got a mem address.
    '''
    def __str__(self) -> str:
        return "A Truck"
