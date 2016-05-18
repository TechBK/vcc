import re

words = {}

file = input("file?")

with open(file, mode='r') as f:
    k = []
    for line in f:
        k.append(re.split("\W+", line))
        # print(k)

i = 0
for line in k:
    if line:
        i += 1
        for word in line:
            word = word.lower()
            if word != '':
                if word in words:
                    words[word]['number'] += 1
                    words[word]['line'].append(i)
                else:
                    words[word]= {'number': 1,
                                 'line': [i,]
                                 }


for word, value in sorted(words.items()):
    print(value['number'], word, value['line'])