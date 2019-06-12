class PolishWordnetParser:

    __LEXICAL_UNIT = 'lexical-unit'

    def __init__(self, version):
        self.version = version

    def lexical_unit(self):
        return self.__LEXICAL_UNIT
