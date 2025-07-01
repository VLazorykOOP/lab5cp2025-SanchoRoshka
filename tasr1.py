import matplotlib.pyplot as plt
import numpy as np

def hermite_curve(p1, p2, v1, v2, num_points=100):
    t = np.linspace(0, 1, num_points)
    h1 = 2 * t**3 - 3 * t**2 + 1
    h2 = -2 * t**3 + 3 * t**2
    h3 = t**3 - 2 * t**2 + t
    h4 = t**3 - t**2

    x = h1 * p1[0] + h2 * p2[0] + h3 * v1[0] + h4 * v2[0]
    y = h1 * p1[1] + h2 * p2[1] + h3 * v1[1] + h4 * v2[1]

    return x, y

# Точки та вектори
P1 = (1, 1)
P2 = (4, 1)
V1 = (2, 3)
V2 = (2, -3)

x, y = hermite_curve(P1, P2, V1, V2)

plt.figure(figsize=(6, 4))
plt.plot(x, y, 'r-', label='Крива Ерміта')
plt.plot(*P1, 'go', label='P1')
plt.plot(*P2, 'bo', label='P2')
plt.quiver(*P1, *V1, angles='xy', scale_units='xy', scale=1, color='g', label='V1')
plt.quiver(*P2, *V2, angles='xy', scale_units='xy', scale=1, color='b', label='V2')
plt.legend()
plt.title("Крива Ерміта")
plt.axis('equal')
plt.grid(True)
plt.show()
