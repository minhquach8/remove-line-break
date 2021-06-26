import re

with open('mytext.txt', 'r') as file:
    data = file.read()

# print(data)

pars = []

word = re.sub(r'someword=|\,.*|\#.*', '', data)
word = re.sub(r'\n', ' ', word).strip()
word = re.sub(r'  ', '\n\n', word).strip()
pars.append(word)

outF = open("mytext.txt", "w")
for k in pars:
    outF.write(k)
outF.close()
