largest = 0
smallest = 9999999

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break;
        n = int(num)
    except:
        print ("Invalid input")
    largest = n if largest < n else largest
    smallest = n if smallest > n else smallest

print ("Maximum is",largest)
print ("Minimum is",smallest)