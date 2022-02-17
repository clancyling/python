name = input("Enter file:")
if len(name) < 1:
    # should be "mbox-short.txt"
    name = "mbox-short.txt.txt"
handle = open(name)
# create a dictionary to hold hours as keys, and occurences as values
hour_stat = {}
for line in handle:
    if line.startswith('From '):
        # extract the second to last element as time and split it again to get the hour
        hour = line.split(" ")[-2].split(":")[0]
        # store the hour as key into the dictionary hour_stat
        if hour in hour_stat:
            hour_stat[hour] += 1
        else:
            hour_stat[hour] = 1
# use an extra list to sort the keys of hours, and use it to get the count
hour_key_sorted = sorted(hour_stat.keys())
for hour in hour_key_sorted:
    print(hour, hour_stat[hour])