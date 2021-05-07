with open('hpmor.txt', 'r') as reader:
	all_lines = reader.readlines()

new_lines_inters = []
new_lines = []

import re

pattern = '\*{1,3}'
other_pattern = '\d{1,}\s\*'




for line in all_lines:
	result = re.match(pattern, line)
	other_result = re.match(other_pattern, line)
	if '' not in line and not line.isupper() and not result and not line.lstrip().rstrip().isdecimal():
		if line == '\n':
			new_lines_inters.append(line)
		else:	
			new_lines_inters.append(line.rstrip('\n'))

for new_lines_inter in new_lines_inters:
	if new_lines_inter != "\n":
		new_lines.append(new_lines_inter)


train_number = 60000
dev_number = 4000
test_number = 3,118


with open('hpmor_train.txt', 'w+') as writer:
	for line in new_lines[0:30000]:
		writer.write(line)
	for line in new_lines[37118:67118]:
		writer.write(line)


with open('hpmor_dev.txt', 'w+') as writer:
	for line in new_lines[30000:32000]:
		writer.write(line)
	for line in new_lines[35118:37118]:
		writer.write(line)

with open('hpmor_test.txt', 'w+') as writer:
	for line in new_lines[32000:35118]:
		writer.write(line)




