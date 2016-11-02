import xml.etree.ElementTree as ET

root = ET.parse('merged.xml').getroot()
data_tsv = open('/home/feasinde/Git/COMP490/dataset/dataset_en.tsv', 'w')
data_tsv.write('en\tfr\n')
for speaker in root:
    for chunk in speaker:
        if chunk.getchildren() != []:
            connectives = [x.text for x in chunk[0]]
            sentence = [x for x in chunk[0].itertext()]
            fr_sentence = ''.join(chunk[1].itertext())  + '\n'
            for connective in connectives:
                mod_sentence = list(sentence)
                index_of_connective = mod_sentence.index(connective)
                mod_sentence[index_of_connective] = mod_sentence[index_of_connective].upper()
                data_tsv.write(''.join(mod_sentence) +'\t'+fr_sentence)
data_tsv.close()
