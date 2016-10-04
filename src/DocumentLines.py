"""docstring for module"""

import re

class EnglishSentences():
    """docstring for EnglishSentence."""
    def __init__(self, en_string):
        self.line = en_string
        self.connectives_dict = {}

    def add_connective(self, en_connective, fr_connective):
        """Adds dictionary entry as corresponding en/fr connectives"""
        self.connectives_dict[en_connective] = fr_connective

    def get_line(self):
        """Returns the text of the current line"""
        return self.line

    def get_connectives(self):
        """Returns connectives_dict"""
        return self.connectives_dict

    def get_connectives_lst(self):
        """Returns list of connectives"""
        return re.findall("\*\*(.*)\*\*", self.get_line())

class FrenchSentences():
    """docstring for FrenchSentences"""
    def __init__(self, fr_string):
        self.line = fr_string

    def get_line(self):
        """Returns the text of the current line"""
        return self.line
