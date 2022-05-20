# Lists

name = input("Enter file name: ")
fh = open(name)
lst = list()
for line in fh :
    line=line.rstrip()
    a = line.split()
    for word in a :
        if word in lst :
            continue
        else :
            lst.append(word)
lst.sort()
print(lst)
