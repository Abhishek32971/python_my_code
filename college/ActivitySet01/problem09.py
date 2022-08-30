# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
y=0
count=0
y=float(y)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    n=line.find("0.")
    x=float(line[n:])
    y=x+y
    count=count+1
average=y/count
print("Average spam confidence:",average)