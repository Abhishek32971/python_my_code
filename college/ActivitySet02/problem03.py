

def get_cs():
    a=(input("enter a string"))
    return a


def cs_to_lot(cs):
    a=cs.split(";")
    j=list()
    for i in a:
        b=i.split("=")
        j.append(b)
    j.pop()
    return j

    


def main():
    cs = get_cs()
    j=cs_to_lot(cs)
    print(j)
    


main()
