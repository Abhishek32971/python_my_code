'''
import math
def smallest2(a,b,c):
    if a<b and c<b:
        print(a,c)
        return a,c
    elif b<a and c<a:
        print(b,c)
        return b,c
    else :
        print(a,b)
        return a,b 
def dista(x1,y1,x2,y2):
    d=math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    print(d)
    return d
def main():
    i=int(input('enter the number of times you want to exectute the loop'))
    while i!=0:
        #x1,x2,x3,y1,y2,y3=int(),int(),int(),int(),int(),int()
        x1,y1,x2,y2,x3,y3=input(""),input(""),input(),input(),input(),input()
        x1,x2,x3,y1,y2,y3=float(x1),float(x2),float(x3),float(y1),float(y2),float(y3)
        a=dista(x1,y1,x2,y2)
        b=dista(x2,y2,x3,y3)
        c=dista(x1,y1,x3,y3)
        z,t=smallest2(a,b,c)
        area=z*t
        print("Area of rectangle with vertices (%.1f,%.1f),(%.1f,%.1f),(%.1f,%.1f) is %.1f" %(x1,y1,x2,y2,x3,y3,area))
        i-=1

main()
print("thankyou for choosing me to execute your math problem!!!\n")
'''
class Rectangle:
    def __init__(self, veritces: list[tuple[float, float]]):
        self.v1, self.v2, self.v3 = veritces
        self.l, self.b = self.get_l_b()

    def get_l_b(self):
        x = ((self.v2[0] - self.v1[0]) ** 2 + (self.v2[1] - self.v1[1]) ** 2) ** 0.5
        y = ((self.v3[0] - self.v2[0]) ** 2 + (self.v3[1] - self.v2[1]) ** 2) ** 0.5
        z = ((self.v1[0] - self.v3[0]) ** 2 + (self.v1[1] - self.v3[1]) ** 2) ** 0.5

        if x >= y and x >= z:
            return y, z
        elif y >= z:
            return x, z
        else:
            return x, y

    def find_area(self):
        return self.l * self.b


class Rectangles(list):
    def __init__(self, rects: list[list[tuple[float, float]]]):        
        super().__init__(Rectangle(r) for r in rects)


def inp_rects():
    while True:
        try:
            n = int(input())
            assert n > 0
            break
        except:
            print("Enter a valid number of rectangles.")
            continue
 
    i = 0
    lst = []
    while True:
        try:
            nums = [float(_) for _ in input().strip().split()]
        except:
            print("Enter valid cartesian coordinates.")
            continue
        
        if (len(nums) != 6):
            print("There should only be 3 vertices with 6 total points.")
            continue
        lst.append([(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])
        i += 1
        if i == n:
            break
        
    return lst
    
    
def output(rects):
    for rect in rects:
        print(f"Area of rectangle with vertices {rect.v1},{rect.v2},{rect.v3} is {round(rect.find_area(), 1)}")


def main():
    r = Rectangles(inp_rects())
    output(r)

if __name__ == "__main__":
    main()