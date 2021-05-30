def prefix(string):
    print("#")
    for i in range(0,len(string)+1):
        print(string[0:i])


def suffix(string):
    for i in range(0,len(string)+1):
        print(string[i:len(string)+1])
    print("#")


def substring(string):
    print("#")
    for i in range(0,len(string)):
        for j in range(i+1,len(string)+1):
            print(string[i:j])

def prop_prefix(string):
    for i in range(0,len(string)):
        print(string[0:i])


def prop_suffix(string):
    for i in range(0,len(string)):
        print(string[i+1:len(string)])


def prop_substring(string):
    for i in range(0,len(string)):
        for j in range(i,len(string)+1):
            if string[i:j] != string:
                print(string[i:j])
            else:
                continue


if __name__ == "__main__":
    string = input("Enter a string:\n")
    opt = int(input("Enter option\n 1.Prefix\n 2.Suffix\n 3.Substring\n 4.Proper prefix\n 5.Proper suffix\n 6.Proper substring\n"))
    if opt == 1:
        prefix(string)
    elif opt == 2:
        suffix(string)
    elif opt == 3:
        substring(string)
    elif opt == 4:
        prop_prefix(string)
    elif opt == 5:
        prop_suffix(string)
    elif opt == 6:
        prop_substring(string)
    else:
        print("Invalid option")