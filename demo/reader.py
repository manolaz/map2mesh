import laspy 
import numpy as np

lidar = laspy.file.File("./data/points.las")
data = np.vstack((lidar.x, lidar.y, lidar.z)).transpose()  

print(data)