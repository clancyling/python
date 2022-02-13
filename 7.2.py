# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tcount = 0
xcount = 0
for line in fh:
    line = line.rstrip()
    tcount = tcount + 1
    if not line.startswith("X-DSPAM-Confidence:"):
        count = xcount + 1
        continue
        count = tcount - xcount
    fline = float(line[19:])
    
    
print("Average spam confidence:", fline / 27)
