

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

def lot_to_cs(lot):
    k=str()
    for (i,j) in lot:
        k=k+(i+"="+j+";")
    return k


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
