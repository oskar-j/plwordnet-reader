import xml.etree.ElementTree as ET

from plwordnet import PolishWordnetDataset
from plwordnet.parser import PolishWordnetParser


class PolishWordnet:

    def __init__(self, resource=None):
        if resource is None:
            self.resource = PolishWordnetDataset()
        elif type(resource) is str:
            self.resource = PolishWordnetDataset(location=resource)
        elif type(resource) is PolishWordnetDataset:
            self.resource = resource
        else:
            raise NotImplementedError("The 'resource' attribute must be of plwordnet.PolishWordnetDataset type")

        self.parser = PolishWordnetParser(self.resource.get_version())

    def load(self):
        tree = ET.parse(self.resource.get_location())
        root = tree.getroot()

        lexical_units = root.findall(self.parser.lexical_unit())
