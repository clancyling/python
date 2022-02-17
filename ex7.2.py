# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
num_legit_lines = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num_legit_lines += 1
    total += float(line[19:])
print("Average spam confidence:", total / num_legit_lines)