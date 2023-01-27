from pprint import pprint


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def dump(data):
        print("-----------------------------------")
        pprint(vars(data))
        print("-----------------------------------")