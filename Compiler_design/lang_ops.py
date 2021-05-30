def union(s1,s2):
    print(s1 | s2)


def intersect(s1,s2):
    print(s1 & s2)


def concat(s1,s2):
    for i in s1:
        for j in s2:
            print(i+j)


if __name__ == "__main__":
    string1 = input("Enter a list elements separated by space\n")
    list1 = string1.split()
    s1 = set(string1.split())
    string2 = input("Enter another list elements separated by space\n")
    list2 = string2.split()
    s2 = set(string2.split())
    opt = int(input("Enter option\n 1.Union\n 2.Intersection\n 3.Concatenation\n"))
    if opt == 1:
        union(s1, s2)
    elif opt == 2:
        intersect(s1, s2)
    elif opt == 3:
        concat(list1, list2)
    else:
        print("Invalid option")