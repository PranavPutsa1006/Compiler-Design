def reverse(s1):
    s2 = set()
    for s in s1:
        s=s[::-1]
        s2.add(s)
    return s2


def union(s1,s2):
    print(s1 | s2)


def concat(w,s2):
    s = set()
    for i in s2:
        s.add(w+i)
    return s

if __name__ == "__main__":
    string1 = input("Enter language L1\n")
    list1 = string1.split()
    s1 = set(string1.split())
    string2 = input("Enter language L2\n")
    list2 = string2.split()
    s2 = set(string2.split())
    w = input("Enter string w\n")
    
    print("W = "+w)
    print(s1)
    print(s2)
    print(reverse(s1))
    print(concat(w, s2))
    print("Final Output: ")
    print(union(reverse(s1),concat(w,s2)))
    