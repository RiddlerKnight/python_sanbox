class Wizard:
    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError("Name is empty")
        self.name = name
...

class Professor(Wizard):
    def __init__(self, name: str, subjent: str) -> None:
        super().__init__(name)
        self.subject = subjent
...

class Student(Wizard):
    def __init__(self, name: str, house: str) -> None:
        super().__init__(name)
        self.house = house
...
