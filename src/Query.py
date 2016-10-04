"""Query performs a comparison between an set of parallel English sentences and
a French sentences and saves the result to a file"""

from DocumentLines import EnglishSentences, FrenchSentences

NUMBER_OF_LINES_TO_BE_READ = 10

class Query():
    """Performs a comparison between a set of parallel English sentences and
    French sentences"""
    def __init__(self, en_filepath, fr_filepath):
        self.english_lines = []
        self.french_lines = []
        self.line_number = 6
        with open(en_filepath) as en_file:
            for i in range(NUMBER_OF_LINES_TO_BE_READ):
                self.english_lines.append(EnglishSentences(en_file.readline()))
        with open(fr_filepath) as fr_file:
            for i in range(NUMBER_OF_LINES_TO_BE_READ):
                self.french_lines.append(FrenchSentences(fr_file.readline()))

    def print_line(self):
        """Outputs an instance of parallel sentences and increases the line counter by 1"""
        print("The English sentence is:\n")
        print('"' + self.english_lines[self.line_number].get_line()[:-1] + '"\n')
        print("The French sentence is:\n")
        print('"' + self.french_lines[self.line_number].get_line()[:-1] + '"\n')
        # self.line_number += 1

    def question(self):
        """Displays parallel sentences and queries user for equivalent connectives"""
        connectives = self.english_lines[self.line_number].get_connectives_lst()
        self.print_line()
        for connective in connectives:
            print('Find the equivalent of the word "' + connective + '" in the French sentence: ')
            fr_connective = input()
            self.english_lines[self.line_number].add_connective(connective, fr_connective)
        print(self.english_lines[self.line_number].get_connectives(),"\n")

    def next_line(self):
        self.line_number += 1
