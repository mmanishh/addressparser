class AddressFlagger:

    def __init__(self):
        pass

    def check(self, address, tags):
        if isinstance(address, dict):
            return all(elem in list(address.keys()) for elem in tags)
        else:
            raise TypeError("address param should be dictionary.")
