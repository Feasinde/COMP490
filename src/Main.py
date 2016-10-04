"""Main script"""

from Query import Query

ENGLISH_DOCUMENT_FILE_PATH = "/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl_bold.en"
FRENCH_DOCUMENT_FILE_PATH = "/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl_bold.fr"

query = Query(ENGLISH_DOCUMENT_FILE_PATH, FRENCH_DOCUMENT_FILE_PATH)
query.question()
query.next_line()
query.question()
query.next_line()
query.question()
