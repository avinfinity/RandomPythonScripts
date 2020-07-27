import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import axes3d

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)

print(x)

plt.title("Sine Wave Form")
plt.plot(x,y)
plt.show()

df = pd.DataFrame(np.random.rand(10,5), columns=['A','B','C','D','E'])

plt.boxplot(df)
plt.show()

chart = plt.figure()
chart3d = chart.add_subplot(111,projection='3d')
X,Y,Z = axes3d.get_test_data(0.08)
chart3d.plot_wireframe(X,Y,Z,color='r',rstride=15,cstride=10)

plt.show()