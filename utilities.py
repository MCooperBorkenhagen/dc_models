import numpy as np

def load(filename,dtype=np.dtype('float'),simplify=False):
    def dropUnusedUnits(x):
        z = np.any(x,axis=0)
        return x[:,z]
    
    with open(filename) as f:
        ex = np.array([x.strip('\n').split(',') for x in f.readlines()],dtype=dtype)

    if simplify:
        ex = dropUnusedUnits(ex)

    return ex