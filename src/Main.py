"""Main script"""

from Query import Query
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
ENGLISH_DOCUMENT_FILE_PATH = os.path.join(__location__, 'europarl_bold_short.en')
FRENCH_DOCUMENT_FILE_PATH = os.path.join(__location__, 'europarl_bold_short.fr')

query = Query(ENGLISH_DOCUMENT_FILE_PATH, FRENCH_DOCUMENT_FILE_PATH)
query.question()
query.next_line()
query.question()
query.next_line()
query.question()
