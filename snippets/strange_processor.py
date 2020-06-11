from Kelvin.business.oo import OnlyOne


class StrangeProcessor(object):
    def __init__(self):
        self.onlyone = OnlyOne()

    def exec(self):
        print(f'Value = {self.onlyone.get_value()}')