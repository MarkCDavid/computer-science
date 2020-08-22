filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()

words = list()
for line in file_handle:
    split_words = line.split()
    for word in split_words:
        if word not in words:
            words.append(word)
words.sort()
print(words)
