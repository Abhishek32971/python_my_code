'''def inptlst():
    while(t):
        a=input("enter the number of values")
        x=a.split()
    
        try:
            len(x)==a
            for i in x:
                i=int(i)
        except:
            print("the length of the string is not the right value , kindly enter the right value")
            continue
        t-=1
    a=input("enter the number of values")
    y=input("enter the values")

    try:
        x=y.split()
        len(x)==a
        y=list()
        for i in x:
            y.append(int(i))
    except:
        print("the length of the string is not the right value , kindly enter the right value")
        inptlst()
    return y

def finllst(x):
    y=list()
    i=0
    while(i<len(x)):
        if(x[i]==0):
            if(x[i+1]==0):
                y.append(0)
                i+=2
                continue
            else:#if(x[i+1]!=0 ):#and x[i+2]!=0):
                if (x[i+2]!=0):
                    for j in range(x[i+1]):
                        y.append(x[i+2])
                    i+=3
                    continue
                else :
                    y.append(x[i])
                    y.append(x[i+1])
                    y.append(x[i+2])
                    i+=3
                    continue
        else:
            y.append(x[i])
            i+=1
            continue

    ''' '''elif(x[i]!=0):
            if(x[i+1]!=0):
                if(x[i+2]!=0):
                    y.append(x[i])
                    y.append(x[i+1])
                    y.append(x[i+2])
                    i+=3
                    print(y)
                    continue
                y.append(x[i],x[i+1])
                i+=3
                print(y)
                continue
            y.append(x[i])
            i+=1
            print(y)
    
    return y

        


         

def main():
    t=int(input("enter the number values you want to enter"))
    for i in range(t):
        x=inptlst()
        print(x)
        y=finllst(x)
        print(y)
        t-=t


main()
'''




def decode(s: list[int]):
    res = ''
    i = 0
    while i < len(s):
        if s[i] == 0:
            if s[i + 1] == 0:
                res += '0 '
                i += 2
            else:
                n = s[i + 1]
                c = s[i + 2]
                for _ in range(n):
                    res += f'{c} '
                i += 3

        else:
            res += f'{s[i]} '
            i += 1

    return res


def input_code():
    while True:
        try:
            n = int(input().strip())
            assert n > 0
            break
        except:
            print("Enter a valid positve integer")
            continue

    inp = []
    for _ in range(n):
        while True:
            try:
                m = int(input().strip())
                assert m > 0
                break
            except:
                print("Enter a valid positive length of the code")
                continue

        while True:
            try:
                code = [int(i) for i in input().strip().split()]
                if len(code) != m:
                    print("Please enter correct number of integers")
                    continue
                break
            except:
                print("Please enter only integers")
                continue

        inp.append(code)

    return inp


def main():
    for i in input_code():
        print('\n')
        print(*i)
        print(decode(i) + '\n')


if __name__ == "__main__":
    main()