def euclidean_dist(x, y):
    n = len(x)
    if n == 0:
        raise ValueError()
    else:
        res_dist = 0
        for i in range(n):
            dist = abs(x[i] - y[i])
            dist_n = dist**n
            res_dist+=dist_n # sum
        n_root = 1/(n) # nth root
        res = res_dist**(n_root)
        return res

def manhattan_dist(x, y):
    raise NotImplementedError()

def jaccard_dist(x, y):
    raise NotImplementedError()

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
# if __name__ == '__main__':
#     x = [0,0]
#     y = [0,1]
#     euclidean_dist(x,y)