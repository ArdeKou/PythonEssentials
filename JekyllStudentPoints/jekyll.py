from os import strerror, stat
# Exceptions
class StudentsDataException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class BadLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

# ask for file name
try:
    src = input('Give source .txt file: ')
    if stat(src).st_size == 0:
       raise FileEmpty('The file is empty')
except FileEmpty as fe:
    print(fe, ':', src)
    exit()
except FileNotFoundError as e:
    print(strerror(e.errno))
    exit()
    
# Read file contents
students = {}
try:
    rf = open(src, 'rt')
    line = rf.readline()
    if not ''.join(line.split()).isalnum():
        raise BadLine('Bad line')
    while line != '':
        # sum points
        split = line.split()
        name = split[0] + ' ' + split[1]
        if name in students:
            students[name] += float(split[2])
        else:
            students[name] = float(split[2])
        line = rf.readline()
    rf.close()
except IOError as e:
    print('I/O Error occured: ', strerror(e.errno))
except BadLine as bl:
    print(bl, ':', line)

#sort and print
for key in sorted(students):
    print(key,'\t', students[key])