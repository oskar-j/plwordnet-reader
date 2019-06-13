class PolishWordnetParser:

    __LEXICAL_UNIT = 'lexical-unit'
    __SYNSET_UNIT = 'synset'

    __LEXICAL_RELATIONS = 'lexicalrelations'
    __SYNSET_RELATIONS = 'synsetrelations'

    def __init__(self, version):
        self.version = version

    def lexical_unit(self):
        return self.__LEXICAL_UNIT

    def synset_unit(self):
        return self.__SYNSET_UNIT

    def lexical_relations(self):
        return self.__LEXICAL_RELATIONS

    def synset_relations(self):
        return self.__SYNSET_RELATIONS
