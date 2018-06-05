import xml.etree.ElementTree as ET
import six


class PolishWordnet:

    def __init__(self, resource=None):
        self.resource = resource

    def load(self):
        tree = ET.parse(self.resource)
        root = tree.getroot()
        six.print_(root)
