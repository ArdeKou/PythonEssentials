from os import strerror, path
#creates a histogram of letters in a text file
#user input
#use the .txt files in the directory for error results demonstrations
src = input('Give .txt filename: ')
hist = path.splitext(path.basename(src))[0] + '.hist' #savefile name parse

#read data
data = ''
try:
    rf = open(src, 'rt')
    data = rf.read()
    rf.close
except IOError as e:
    print('I/O error', strerror(e.errno))

#parse
alpha = {}
for a in range(25):
    alpha[chr(65+a)] = 0

for char in data:
    if char.isalpha():
        alpha[char.upper()] += 1

#sort, print and save
try:
    of = open(hist, 'wt')
except IOError as e:
    print('I/O error', strerror(e.errno))

for key, value in sorted(alpha.items(), key=lambda kv: kv[1] , reverse=True):
    if value > 0:
        print('{} -> {}'.format(key, value))
        of.write('{} -> {}\n'.format(key, value))

of.close()
