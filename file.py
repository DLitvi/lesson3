with open('referat.txt', 'r', encoding = 'utf-8') as file:
	word_count = 0
	for line in file:
		line = line.split()
		word_count += len(line)
	print(word_count)
