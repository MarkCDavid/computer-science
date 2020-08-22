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
    hour = line.split()[5].split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1

hour_counts = [(key, counts[key]) for key in counts]
hour_counts.sort()
for hour_count in hour_counts:
    print(hour_count[0], hour_count[1])


