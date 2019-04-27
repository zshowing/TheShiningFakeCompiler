import random
import time
import re

word = "All work and no play makes Jack a dull boy."
typos = {'a': "qwsz",   'b': "vghn",   'c': "xdfv",
         'd': "serfcx", 'e': "wsdfr",  'f': "dcvgtr",
         'g': "fvbhyt", 'h': "gbnjuy", 'i': "ujko",
         'j': "hnmklu", 'k': "jmloi",  'l': "mkop",
         'm': "njkl",   'n': "bhjm",   'o': "iklp",
         'p': "ol",     'q': "wa",     'r': "edft",
         's': "wazxde", 't': "rfgy",   'u': "yhji",
         'v': "cfgb",   'w': "qase",   'x': "zsdc",
         'y': "tghu",   'z': "asx",    ' ': " ",   '.': "."}

def typoGenerator(input):
# decide which type of error to produce
# 1. Reversed letters  (e.g. "Please join me for lnuch")        50%
# 2. Wrong letters (nearby) (e.g. "Please join me for lumch")   10%
# 3. Missing letters  (e.g. "Please join me for luch")          20%
# 4. Extra letters (nearby)  (e.g. "Please join me for lunmch") 10%
# 5. Missing space (e.g. "Please joinme for lunmch") 			10%
	time.sleep(random.random() * 0.5)
	output = ""

	normal = random.random() < 0.4

	if not normal:
		type = random.random()
		if type < 0.1:
			index = random.randint(0, len(input) - 1)
			extra = typos[word[index].lower()]
			output =  input[:index] + random.choice(extra) + input[index:]
			# print "Extra letters"
		elif type < 0.3:
			index = random.randint(0, len(input) - 1)
			output =  input[:index] + input[index + 1:]
			# print "Missing letters"
		elif type < 0.4:
			index = random.randint(0, len(input) - 1)
			wrong = typos[word[index].lower()]
			output =  input[:index] + random.choice(wrong) + input[index + 1:]
			# print "Wrong letters"
		elif type < 0.5:
			spaces = re.finditer(' ', input)
			index = random.choice([space.start() for space in spaces])
			output = input[:index] + input[index + 1:]
			# print "Missing space"
		else:
			index = random.randint(0, len(input) - 2)
			nextWord = input[index + 1]
			inputList = list(input)
			inputList[index + 1] = inputList[index]
			inputList[index] = nextWord
			output = ''.join(inputList)
			# print "Reversed letters"
	else:
		output = input
	return output

with open('log-trim.log') as f:
	for line in f:
		threshold = random.random()
		if threshold < 0.1:
			time.sleep(random.random() * 0.5)
		else:
			time.sleep(random.random() * 0.01)
		print line.rstrip()
	while True:
		print typoGenerator(word)
