def lcs(x, y,m,n):
    if m == 0 or n == 0:
       return 0;
    elif x[m-1] == y[n-1]:
       return 1 + lcs(x, y, m-1, n-1);
    else:
       return max(lcs(x, y, m, n-1), lcs(x, y, m-1, n));


def left_factoring(g):
    com_prod = ""
    factor = ""
    for key in g.copy():
        item = g[key]
        length = len(item[0])
        for prod in item:
            if length>len(prod):
                length = len(prod)
                com_prod = prod
            for prod in item:
                x = lcs(prod, com_prod, len(prod), len(com_prod))
                if length > x:
                    length = x
            if x > 0:
                count=0
                for p in item:
                    count += 1
                    factor = p[0 : length]
                    g[key][count] = p[length:]
            g.update({key+"'": [factor]})
    print(g)
                    
if __name__ == "__main__":
    grammar = {}
    lis = list()
    le = int(input("length"))
    for i in range(0,le):
        key = input("key")
        l = int(input("number of production"))
        lis = list()
        for i in range(0,l):
            lis.append(input())
            grammar.update({key:lis})
    # grammar = {"E":["T+E", "T"], "T":["(E)", "int", "int*T"], "F":["001", "010", "002", "020", "030", "003", "300"]}
    print("Given Grammar:\n",grammar)
    print ("Final Grammar:")
    left_factoring(grammar)