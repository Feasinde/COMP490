import re

# regular expression that matches annotated word
annot_re = re.compile('(.*)__')

# Open documents and retrieve annotated English lines and their
# correspoding French lines.

# en = open('/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl.en')
# fr = open('/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl.fr')
#
# en_an = open('/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl_annotated.en','w')
# fr_an = open('/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl_annotated.fr','w')
#
# for line in en:
# 	if '__' in line:
# 		en_an.write(line)
# 		fr_an.write(fr.readline())
# 	elif '__' not in line:
# 		frLine = fr.readline()
# 		if '__' in frLine:
# 			en_an.write(line)
# 			fr_an.write(frLine)
# 	else:
# 		fr.readline()
# en.close()
# fr.close()
# en_an.close()
# fr_an.close()

# Replace annotations with markdown code for bold font
with open('/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl_bold.fr','w') as en_bold:
	with open('/home/feasinde/Dropbox/Concordia U/research_group_CLaC/europarl_annotated.fr') as en_an:
		for line in en_an:
			l_split_line = line.split()
			for i in range(0,len(l_split_line)-1):
				b_match = re.match(annot_re, l_split_line[i])
				if b_match:
					s_bold_word = '**' + re.findall(annot_re, l_split_line[i])[0] + '**'
					l_split_line[i] = s_bold_word
			s_new_line = ' '.join(l_split_line)+'\n'
			if '_' in s_new_line:
				s_new_line = s_new_line.replace('_',' ')
			en_bold.write(s_new_line)
