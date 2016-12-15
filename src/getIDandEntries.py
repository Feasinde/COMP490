import csv
import re

csv_file = open("C:/Users/Andrés Lou/Desktop/f968945_2.csv")
results = csv.DictReader(csv_file)

marker_re = re.compile('\<b\>(.*)\</b\>')

id_dict = {}
id_current = ''
en_marker = ''
id_annotations = []
id_distributions = {}
id_frequencies = {}

## Retrieve _unit_id and associate each unit with a list of entries
for row in results:
    ## Check if current id is the same as the previous id, otherwise 
    ## set the current id to the unit id in the current row
    if not en_marker == row['en']:
        en_marker = row['en']
        id_annotations = []
    id_annotations.append(row['copy_and_paste_the_corresponding_french_marker_enter_a_period_if_there_is_none_'])
    id_dict[row['_unit_id'] + ',' + re.findall(marker_re, en_marker)[0]] = id_annotations

## Retrieve the number of instances of each anwer per unit
for unit in id_dict:
    number_of_instances = {}
    for marker in id_dict[unit]:
        if not marker in number_of_instances:
            number_of_instances[marker] = 1
        else:
            number_of_instances[marker] += 1
    id_distributions[unit] = number_of_instances

## Calculate the relative frequencies of each answer per unit
for unit in id_distributions:
    frequencies = {}
    freq_sum = 0
    ## get total number of entries
    for marker in id_distributions[unit]:
        freq_sum += id_distributions[unit][marker]
    ## get relative frequencies of each marker
    for marker in id_distributions[unit]:
        frequencies[marker] = (id_distributions[unit][marker], id_distributions[unit][marker] / freq_sum)
    id_frequencies[unit] = frequencies

##Write to file
with open('C:/Users/Andrés Lou/Desktop/en_discourse_markers_RF.csv','w') as output:
    output.write('unit_id,en_marker,fr_marker,number_of_workers,relative_frequency\n')
    for unit in id_frequencies:
        for marker in id_frequencies[unit]:
            output.write(unit + ',')
            output.write(marker + ',')
            output.write(str(id_frequencies[unit][marker][0]) + ',' + str(id_frequencies[unit][marker][1]))
            output.write('\n')
