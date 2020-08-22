text = "X-DSPAM-Confidence:    0.8475";
space = text.find(' ')
number = text[space+1:].strip()
print(float(number))