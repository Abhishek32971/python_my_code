def input_two_numbers():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    return a,b
def add(a, b):
    return a+b


def output(a, b, sum):
    print("the sum of the two",a,b,"numbers is ",sum)


def main():
    a, b = input_two_numbers()
    sum = add(a, b)
    output(a, b, sum)
main()
