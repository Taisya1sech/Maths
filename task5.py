#трехмерный график двух параллельных плоскостей
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (11, 11))
ax = Axes3D(fig)
X = np.arange(-13, 13, 2)
Y = np.arange(-13, 13, 2)

X, Y = np.meshgrid(X, Y)

Z = 7*X + 104
Z2 = 7*X + 9
ax.plot_wireframe(X, Y, Z, linestyle='--', linewidth=1)
ax.plot_wireframe(X, Y, Z2,colors='purple')

#трехмерный график поверхностей второго порядка
fig = plt.figure(figsize = (10, 10))
ax = Axes3D(fig)

a = 10
b = 45

X, Y = np.meshgrid((np.arange(-15, 15, 2)), (np.arange(-15, 15, 2)))

Z = b ** 2 + (b ** 2 * (X ** 2 / a ** 2))
Z1 = -(b ** 2 + (b ** 2 * (X ** 2 / a ** 2)))
Z2 = 2*a*X ** np.cos(20) + np.sqrt(2*a*X ** np.cos(20))
ax.plot_surface(X, Y, Z,  linewidth=1, color='b')
ax.plot_surface(X, Y, Z1,  linewidth=1, color='b')

u = np.linspace(-0,8*np.pi, 24)
v = np.linspace(0, np.pi, 12)

x = 5 * np.outer(np.cos(u), np.sin(v))
y = 25 * np.outer(np.sin(u), np.sin(v))
z = -50 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, rstride=4, cstride=4, color='purple')


show()

