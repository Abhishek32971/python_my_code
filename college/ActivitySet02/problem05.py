

def get_cs():
    a=(input("enter a string"))
    return a


def cs_to_dict(cs):
    a=cs.split(";")
    j=list()
    for i in a:
        b=i.split("=")
        j.append(b)
    j.pop()
    thisdict=dict()
    for (i,j) in j:
        thisdict.update({i:j})
    return thisdict



def dict_to_cs(d):
    k=str()
    for i in d:
        k=k+(i+"="+d[i]+";")
    return k


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
