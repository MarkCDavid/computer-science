filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()

counts = dict()
for line in file_handle:
    if not line.startswith("From "):
        continue
    email = line.split()[1]
    counts[email] = counts.get(email, 0) + 1

largest = None
for key in counts:
    if largest == None or counts[key] > counts[largest]:
        largest = key

print(largest, counts[largest])
