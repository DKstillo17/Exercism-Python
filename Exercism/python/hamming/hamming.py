def distance(a,b):
    if len(a) != len(b):
        raise ValueError("DNA strands not the same length!")

    return sum(1 for i in range(len(a)) if a[i] != b[i])
