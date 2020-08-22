filename = input("Filename: ")

try:
    file_handle = open(filename, 'r')
except:
    print("Invalid file name!")
    quit()

def extract_parameter(text):
    space = text.find(' ')
    return float(text[space+1:].strip())

lines = 0
total = 0.0
for line in file_handle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lines += 1
    total += extract_parameter(line)

print("Average spam confidence", total/lines)