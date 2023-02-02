from domains.wheel import Wheel


class Wheels:

    def __init__(self, fl: Wheel, fr: Wheel, rr: Wheel, rl: Wheel):
        self.rl = rl
        self.rr = rr
        self.fr = fr
        self.fl = fl
