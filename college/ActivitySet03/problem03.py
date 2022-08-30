'''def dictofallcom(a):
    d=dict()
    l=-1
    for i in a:
        if l==len(a)-3:
            break
        o=list()                           #create list to add all possible combinations 
        l=l+1                              #::::l::::; is used to indicate the perticular index 
        for j in range(l+2,len(a)):        #add all possible combinations form that index till end of string length(3 or more)
            o.append(a[l:j+1])
        d[l]=o                             #add individual list to dictionary with key as the index
    print(d)           
    return d


def isPalindrome(s):
    return s == s[::-1]


def output(l):
    for i in l:
        for p in range(len(l[i])):
            if isPalindrome(l[i][p]):
                print(i,l[i][p])


def main():
    z=int(input("enter the length of string"))
    a=input("enter the string")
    l=dictofallcom(a)
    output(l)


main()
'''



class Palindrome:
    def __init__(self, w: str):
        self.w = w
        self.palindromes = []
        self.find_palindromes()
    
    @staticmethod
    def is_palindrome(s: str):
        if False in (s[i] == s[j] for i, j in zip(range(0, len(s) // 2), range(len(s) - 1, len(s) // 2 - 1, -1))):
            return False
        return True
    
    def find_palindromes(self):
        i = 0
        j = 2
        l = len(self.w)
        while i <  l - 2:
            if Palindrome.is_palindrome(tmp := self.w[i: j + 1]):
                self.palindromes.append((i + 1, tmp))
            j += 1
            
            if j == l:
                i += 1
                j = i + 2
    

def input_pdromes():
    while True:
        try:
            n = int(input())
            assert n > 0
            break
        except:
            print("Enter a valid integer greater than 0")
            continue
        
    pdromes = []    
    for _ in range(n):
        while True:
            try:
                m = int(input())
                assert m > 0
                break
            except:
                print("Enter a valid length for the string")
                continue
            
        while True:
            s = input().strip()
            if len(s) != m:
                print("Length of the string should match")
                continue
            pdromes.append(Palindrome(s))
            break
    return pdromes
            
            
def output(pdromes):
    print('\n')
    for pdrome in pdromes:
        print(pdrome.w)
        for i, p in pdrome.palindromes:
            print(i, p)
        print("\n")
                
                
def main():
    pdromes = input_pdromes()
    output(pdromes)

if __name__ == "__main__":
    main()                