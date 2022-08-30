smallest =None
largest=None
while True:
    try:
        x=(input("enter the number"))
        if x=="done":
            break
        x=int(x)
        
    except:
        print("invalid input")
        continue
    if smallest==None or x<smallest:
        smallest=x
    if largest==None or x>largest:
        largest=x
print("the largest number is ",largest)
print("the smallest number is ",smallest)
