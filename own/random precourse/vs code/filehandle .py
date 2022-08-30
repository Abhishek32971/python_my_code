fhand=open("t.txt")
count=0
for line in fhand :
    count=count+1
for line in fhand:
    if line.startswith("open"):
        count=count-1
fhand.write("line here\n")
fhand.close()