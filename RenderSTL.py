import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot


######Code taken from 
#https://w.wol.ph/2015/07/10/rendering-stl-files-matplotlib-numpy-stl/

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('E:\\Volumes\\separated_part_0.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()