def diff(a,b):
    b = set(b)
    return [aa for aa in a if aa not in b]

def intersection(a,b):
    b = set(b)
    return [aa for aa in a if aa in b]
