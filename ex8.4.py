fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    # remove trailing whitespaces and \n
    words = line.rstrip().split(" ")
    for word in words:
        if word not in lst:
            lst.append(word)
# sort the list in place
lst.sort()
print(lst)
