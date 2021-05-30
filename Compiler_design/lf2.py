from itertools import izip_longest

def find_prefixes(strings):
    zipped = izip_longest(*strings, fillvalue='')
    for index, letters in enumerate(zipped):
        if index == 0:
            prefixes = letters
        else:
            poss_prefixes = [prefix + letters[i] for i, prefix in enumerate(prefixes)]
            prefixes = [prefix if poss_prefixes.count(prefix) == letters.count(prefix)
                        else prefixes[i] for i, prefix in enumerate(poss_prefixes)]
    return set(prefixes)

def find_prefix_suffixes(strings, prefixes):
    prefix_suffix = dict()
    for s in strings:
        for prefix in sorted(list(prefixes), key=lambda x: len(x), reverse=True):
            if s.startswith(prefix):
                if prefix in prefix_suffix:
                    prefix_suffix[prefix].add(s.replace(prefix, '', 1))
                else:
                    prefix_suffix[prefix] = set([s.replace(prefix, '', 1)])
    return prefix_suffix


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
        prefixes = find_prefixes(t1)
        print(find_prefix_suffixes(t1, prefixes))


if __name__ == "__main__":
    n = int(input("How many productions:\n"))
    prod = []
    for i in range(n):
        prod.append(input("Enter production "+str(i+1)+":"))
    remove_lf(prod)