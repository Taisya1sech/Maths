#круг
x = []
x2 = []
y = []
y2 = []

for i in range(3000):
    r = 1500
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(r ** 2 - i ** 2))
    y2.append(-np.sqrt(r ** 2 - i ** 2))

plt.figure(figsize=(7, 7))
plt.plot(x, y, color='b')
plt.plot(x, y2, color='b')
plt.plot(x2, y2, color='b')
plt.plot(x2, y, color='b')
plt.axis('scaled')
plt.show()

#эллипс
x = []
x2 = []
y = []
y2 = []

for i in range(3000):
    a = 70
    b = 140
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y, color='g')
plt.plot(x, y2, color='g')
plt.plot(x2, y2, color='g')
plt.plot(x2, y, color='g')
plt.axis('scaled')
plt.show()

#гиперболы
x = []
x2 = []
y = []
y2 = []

for i in range(1000):
    a = 800
    b = 400
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y, color='b')
plt.plot(x, y2, color='b')
plt.plot(x2, y2, color='b')
plt.plot(x2, y, color='b')
plt.axis('scaled')
plt.show()

