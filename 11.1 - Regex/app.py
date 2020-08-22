import re

filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()

print(sum([int(x) for x in re.findall("\d+", file_handle.read())]))