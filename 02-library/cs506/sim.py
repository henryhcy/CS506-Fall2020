
def euclidean_dist(x, y):

    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    n = len(x) 
    res_dist = 0
    for i in range(n):
        dist = abs(x[i] - y[i])
        dist_n = dist**n
        res_dist+=dist_n # sum
    n_root = 1/(n) # nth root
    res = res_dist**(n_root)
    return res

def manhattan_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    n = len(x) 
    res_dist = 0
    for i in range(n):
        dist = abs(x[i] - y[i])
        res_dist+=dist # sum
    
    return res_dist


def jaccard_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")

    intersect = len(list(set(x).intersection(y)))
    print(intersect)
    union = len(list(set(x).union(y)))
    print(union)
    sim = intersect / union
    res = 1 - sim
    return res

def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    dot = lambda a,b: sum(i*j for i,j in zip(a,b))
    norm = lambda c: dot(c,c)**(1/2)
    cos = dot(x,y) / (norm(x) * norm(y))
    return cos

# Feel free to add more
# if __name__ == "__main__":
    x = [0,0,0]
    y = [1,1,1]
    print(jaccard_dist(x,y))