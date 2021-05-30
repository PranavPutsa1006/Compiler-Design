def remove_lr(prod):
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
        for k in t1:
            if nt[i] == k[0]:
                t2.append(k)
                t1.remove(t1[k])
                t1.append(nt[i]+"\'")
            else:
                continue


if __name__ == "__main__":
    n = int(input("How many productions:\n"))
    prod = []
    for i in range(n):
        prod.append(input("Enter production "+str(i+1)+":"))
    remove_lr(prod)
    
    