class Host:
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def __str__(self) -> str:
        return "Address:" + self.address + ", Port:" + self.port

    def __repr__(self) -> str:
        return "Address:" + self.address + ", Port:" + self.port

    def __eq__(self, other) -> bool:
        return self.address == other.address and self.port == other.port

    def gettuple(self) -> tuple:
        return (str(self.address), int(self.port))