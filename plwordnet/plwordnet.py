import xml.etree.ElementTree as ET

from plwordnet import PolishWordnetDataset
from plwordnet.parser import PolishWordnetParser
from plwordnet.engine import PolishWordnetEngine


class PolishWordnet:

    __IMPLEMENTED_ENGINES = ['XML', 'NEO4J']

    def __init__(self, engine='XML', resource=None):
        if resource is None:
            self.resource = PolishWordnetDataset()
        elif type(resource) is str:
            self.resource = PolishWordnetDataset(location=resource)
        elif type(resource) is PolishWordnetDataset:
            self.resource = resource
        else:
            raise NotImplementedError("The 'resource' attribute must be of plwordnet.PolishWordnetDataset type")

        if type(engine) is str:
            if engine not in self.__IMPLEMENTED_ENGINES:
                raise NotImplementedError('Unrecognized engine, allowed values are "XML" or "NEO4J"')
            else:
                self.engine = PolishWordnetEngine(self.__IMPLEMENTED_ENGINES.index(engine))
        elif type(engine) is type(PolishWordnetEngine):
            self.engine = engine
        else:
            raise NotImplementedError("The 'engine' attribute must be either a string " +
                                      "or of plwordnet.PolishWordnetEngine type")

        self.parser = PolishWordnetParser(self.resource.get_version())

    def load(self):
        tree = ET.parse(self.resource.get_location())
        root = tree.getroot()

        lexical_units = root.findall(self.parser.lexical_unit())
        synset_units = root.findall(self.parser.synset_unit())

        lexical_relations = root.findall(self.parser.lexical_relations())
        synset_relations = root.findall(self.parser.synset_relations())
