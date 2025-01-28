scores = (8, 92, 98, 89, 78)
#operator * in tuple unpacking is used to gather multiple elements from the tuple to list
maximum, *rest = scores 
print(maximum)
print(rest)


def first(b):
    c = list(b)	
    d = range((len(c)))
    e = c[d[0]] + c[d[len(c)-1]]
    print(e)

a = "aim for number 1"
f = first(a)