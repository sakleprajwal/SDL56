def word_count(str):
    count=dict()
    w=str.split()
    for a in w:
        if a in count:
            count[a]+=1
        else:
            count[a]=1

    return count

c=raw_input("Enter the string")
d=word_count(c)
f=sorted(d.items())
print(d)
print(f)

