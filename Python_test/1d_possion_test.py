import numpy as np
import sys
import matplotlib.pyplot as plt
from fealpy.mesh.IntervalMesh import IntervalMesh

n = int(sys.argv[1])

node = np.array([0, 1], dtype=np.float)
cell = np.array([(0, 1)], dtype=np.int)
Imesh = IntervalMesh(node,cell)
Imesh.uniform_refine(n=n)

fig = plt.figure()
axes = fig.gca()
Imesh.add_plot(axes)
Imesh.find_node(axes, showindex=True)
#Imesh.find_edge(axes, showindex=True)
#Imesh.find_cell(axes, showindex=True)
plt.show()
