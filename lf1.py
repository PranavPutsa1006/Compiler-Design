import os


def remove_lf(prod):
    nt = []
    t = []
    for i in prod:
        nt.append(i.split("->")[0])
        t.append(i.split("->")[1])
    print(nt)
    print(t)
    for i in range(len(prod)):
        t1 = t[i].split("|")
        t2 = []
        prefix = os.path.commonprefix(t1)
        print(prefix)
            


if __name__ == "__main__":
    n = int(input("How many productions:\n"))
    prod = []
    for i in range(n):
        prod.append(input("Enter production "+str(i+1)+":"))
    remove_lf(prod)
    
    