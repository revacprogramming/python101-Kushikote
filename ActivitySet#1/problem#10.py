# Dictionaries

filename = "dataset/mbox-short.txt"

name = input("Enter file name: ")
fh = open(name)
words = list()

counts = dict()
for line in fh:
	if line.startswith("From:"):
		words = line.split()
		if words[1] not in counts:
			counts[words[1]] = 1
		else:
			counts[words[1]] += 1

you = counts.values()
me = max(you)
for key in counts:
	if counts[key] == z:
		print(key, z)
    
'''
    

name = input("Enter file:")
fname = open(name)
word = []

counts = dict()
for lines in fname:
	if lines.startswith("From:"):
		word = lines.split()
	if word[1] in counts:
		counts[word[1]] += 1
	else:
		counts[word[1]] = 1

me = counts.value()
you = max(me)
for key in counts:
	if counts(key) == you:
		print(key, you)'''
