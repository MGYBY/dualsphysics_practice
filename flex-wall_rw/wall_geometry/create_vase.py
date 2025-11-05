import gmsh
import sys
import numpy as np

r0 = 0.03
cell_size = r0/12

# ... (read_curve_points function from above) ...

filename = "coords_large.csv"
arr=np.loadtxt(filename, delimiter=',', skiprows=0)
X = arr[:,0]
Y = arr[:,1]

gmsh.initialize()
gmsh.model.add("curve_from_csv")
go = gmsh.model.occ # Shorthand for OCC kernel commands

point_tags = []
for i in range(len(X)):
    p = go.addPoint(0, Y[i], X[i], cell_size) # lc can be adjusted
    point_tags.append(p)

line_tags = []
for i in range(len(X)-1):
    l = gmsh.model.occ.addLine(point_tags[i], point_tags[i+1])
    line_tags.append(l)

curve_loop = gmsh.model.occ.addCurveLoop(line_tags)
# spline_tag = go.addSpline(point_tags)

surface = gmsh.model.occ.addPlaneSurface([curve_loop])

# Rotate {{0,0,1}, {0,0.3,0}, -Pi/4} { Point{5}; }

go.synchronize() # Synchronize the CAD model with Gmsh's internal representation

# Generate mesh (optional, if you want to mesh the curve)
gmsh.model.mesh.generate(1) # Generate 1D mesh for the curve

gmsh.fltk.run() # Open Gmsh GUI to visualize
gmsh.finalize()
