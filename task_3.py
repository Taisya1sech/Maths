#Задание 3.1
import math

def polar2cart(r,phi):
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return x,y

polar2cart(2,45)


#Задание 3.2
phi = np.arange(0., 2., 1./180.)*np.pi

plt.polar(phi, [5]*len(phi))

plt.show()


#Задание 3.3
phi = np.arange(3, 6, 2)
print(phi)
rho = np.arange(3, 6, 2)
print(rho)

plt.polar(phi, rho)

plt.show()
