fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt.txt"

fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    s = line.split(':')
    wordss = s[0]
    words = wordss.split()
    
    
    if not line.startswith('From ') : continue

    
    for word in words:
          if word == words[5]:
              counts[word] = counts.get(word,0) + 1



tmp = list()
for k,v in counts.items() :
#     print(k,v)
    newt = (k, v)
    tmp.append(newt)

tmp = sorted(tmp)
for tuple in tmp:
    print(tuple[0],tuple[1])


# for v,k in tmp[:12] :
#     print(k,v)
