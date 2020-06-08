import numpy as np
from laspy.file import File
inFile = File("./data/points.las", mode = "r")

# Grab all of the points from the file.
point_records = inFile.points

# Grab just the X dimension from the file, and scale it.
def scaled_x_dimension(las_file):
    x_dimension = las_file.X
    scale = las_file.header.scale[0]
    offset = las_file.header.offset[0]
    return(x_dimension*scale + offset)
scaled_x = scaled_x_dimension(inFile)

# Find out what the point format looks like.
print("Examining Point Format: ")
pointformat = inFile.point_format
for spec in inFile.point_format:
    print(spec.name)

#Like XML or etree objects instead?
print("Grabbing xml...")
a_mess_of_xml = pointformat.xml()
an_etree_object = pointformat.etree()

# #It looks like we have color data in this file, so we can grab:
# blue = inFile.blue

#Lets take a look at the header also.
print("Examining Header Format:")
headerformat = inFile.header.header_format
for spec in headerformat:
    print(spec.name)

print("Find close points...")
# Grab the scaled x, y, and z dimensions and stick them together
# in an nx3 numpy array

coords = np.vstack((inFile.x, inFile.y, inFile.z)).transpose()

# Pull off the first point
first_point = coords[0,:]

# Calculate the euclidean distance from all points to the first point

distances = np.sum((coords - first_point)**2, axis = 1)

# Create an array of indicators for whether or not a point is less than
# 500000 units away from the first point

keep_points = distances < 500000

# Grab an array of all points which meet this threshold

points_kept = inFile.points[keep_points]

print("We're keeping %i points out of %i total"%(len(points_kept), len(inFile)))


print("Find ground points...")
# Grab the return_num and num_returns dimensions
num_returns = inFile.num_returns
return_num = inFile.return_num
ground_points = inFile.points[num_returns == return_num]

print("%i points out of %i were ground points." % (len(ground_points),
        len(inFile)))


print("Writing output files...")

outFile2 = File("./data/ground_points.las", mode = "w",
                header = inFile.header)
outFile2.points = ground_points
outFile2.close()