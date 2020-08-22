filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()

count = 0
for line in file_handle:
    if not line.startswith("From "):
        continue
    
    count += 1
    print(line.split()[1])

print("There were", count, "lines in the file with From as the first word")
