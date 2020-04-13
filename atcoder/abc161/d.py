K = int(input())


xs = [str(x) for x in range(1,10)]

def get_lunlun(xs):
    ret = []
    for x in xs:
        last = x[-1]
        if last ==  "0":
            ret.append(x+"0")
            ret.append(x+"1")
        elif last == "9":
            ret.append(x+"8")
            ret.append(x+"9")
        else:
            ret.append(x+ str(int(last)-1))
            ret.append(x+ str(int(last)))
            ret.append(x+ str(int(last)+1))
    return ret

while K > len(xs):
    K = K -  len(xs)
    xs = get_lunlun(xs)
print(xs[K-1])
    
