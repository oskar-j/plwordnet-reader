class PolishWordnetDataset:

    default_locations = {'3.1': '/data/plwordnet_3_1/plwordnet-3.1.xml',
                         '3.0': '/data/plwordnet_3_0/plwordnet-3-0.xml'}

    def __init__(self, version=3.1, location=None):
        self.version = str(version)
        self.location = location

    def get_location(self) -> str:
        if self.location is None:
            return self.default_locations[self.version]
        else:
            return self.location

    def get_version(self) -> str:
        return self.version
