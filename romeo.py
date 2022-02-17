fname = input("Enter file name: ")
fh = open('romeo.txt')
lines = fh.readlines()
for line in lines:
    lines = line.rstrip()
    sines = line.split()
    sines.sort()
    print(sines)

    
