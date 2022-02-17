fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open('mbox-short.txt')
counts = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From ') : continue
    print(words)
    
    for word in words:
          if word == words[5]:
              counts[word] = counts.get(word,0) + 1
print(counts)
tmp = list()
for k,v in counts.items() :
    print(k,v)
    newt = (v,k)
    tmp.append(newt)
print('Flipped',tmp)
tmp = sorted(tmp, reverse=True)

print('Sorted',tmp[:0])
for v,k in tmp[:0] :
    print(k,v)


