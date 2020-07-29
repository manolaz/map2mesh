import laspy
import os 
import glob
import numpy as np
import math




files = glob.glob(os.getcwd() + "/data/*.las")

f_name = "data/out/p1.mesh"

def scale(X, x_min, x_max):
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    print(denom)
    denom = 1 if denom == 0 else denom
    return x_min + nom/denom

def convert(fil):
    lidar = laspy.file.File(fil, mode="r")
    batch_size = 1000000
    idx = 1
        
    data = np.vstack((lidar.x, lidar.y, lidar.z)).transpose()  
    data[:, 0] = scale(data[:, 0], -1, 1)
    data[:, 1] = scale(data[:, 1], -1, 1)
    data[:, 2] = scale(data[:, 2], -3, 3)
    
    with open(f_name, 'a') as fil:
        batches = math.ceil(float(data.shape[0]) / float(batch_size))
        batch_num = 1
        last = 0

        for j in range(0, batches):
            lines = []
            for i in range(last, min(batch_num * batch_size, data.shape[0])):
                l1 = str(idx) + " "
                l2 = str(data[i][0]) + " "
                l3 = str(data[i][1]) + " "
                l4 = str(data[i][2])
                lines.append(l1 + l2 + l3 + l4 + " " + l2 + l3 + l4 + "\n")
                idx += 1
            last += batch_size 
            fil.writelines(lines)
            batch_num += 1

# f = files[0]

convert(files)