from typing import Mapping
from domains.wheels import Wheels


class Truck:

    def __init__(self, name: str, color: str, additional: list[str], profile: Mapping[str, str],
                 wheels: Wheels = None):
        self.profile = profile
        self.additional = additional
        self._name = name
        self._color = color
        self.wheels = wheels

    
    def __str__(self) -> str:
        '''
        if you didn't specify this method, you will got a mem address.
        '''
        return "A Truck"

    @property
    def name(self):
        return self._name
    
    @property
    def name(self):
        return self._color
