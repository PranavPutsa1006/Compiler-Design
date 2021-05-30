def diff(s1,s2):
    print(s1.difference(s2))


def reverse(s1):
    s2 = set()
    for s in s1:
        s=s[::-1]
        s2.add(s)
    print(s2)


def kleene(l1):
    s2 = []
    n = int(input("Enter n:"))
    temp = [i for i in l1]
    for i in range(n):
        if i==0:
            s2.append('#')
            continue
        if i==1:
            s2 = s2 + l1
            continue
        temp = concat(temp,l1)
        s2 = s2 + temp
    print(s2)


def positive(l1):
    s2 = []
    n = int(input("Enter n:"))
    temp = [i for i in l1]
    for i in range(n):
        if i==0:
            s2 = s2 + l1
            continue
        temp = concat(temp,l1)
        s2 = s2 + temp
    print(s2)


def concat(s1,s2):
    list0 = []
    for i in s1:
        for j in s2:
            list0.append(i+j)
    return list0


if __name__ == "__main__":
    opt = int(input("Enter option\n 1.Difference\n 2.Reverse\n 3.Kleene closure\n 4.Positive closure\n"))
    if opt == 1:
        string1 = input("Enter a list elements separated by space\n")
        list1 = string1.split()
        s1 = set(string1.split())
        string2 = input("Enter another list elements separated by space\n")
        list2 = string2.split()
        s2 = set(string2.split())
        diff(s1, s2)
    elif opt == 2:
        string1 = input("Enter a list elements separated by space\n")
        list1 = string1.split()
        s1 = set(string1.split())
        reverse(s1)
    elif opt == 3:
        string1 = input("Enter a list elements separated by space\n")
        list1 = string1.split()
        s1 = set(string1.split())
        kleene(list1)
    elif opt == 4:
        string1 = input("Enter a list elements separated by space\n")
        list1 = string1.split()
        s1 = set(string1.split())
        positive(list1)
    else:
        print("Invalid option")