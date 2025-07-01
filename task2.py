import matplotlib.pyplot as plt
import numpy as np

def koch_curve(ax, p1, p2, order):
    if order == 0:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='blue')
        return

    dx = (p2[0] - p1[0]) / 3
    dy = (p2[1] - p1[1]) / 3

    a = p1
    b = (p1[0] + dx, p1[1] + dy)
    d = (p1[0] + 2 * dx, p1[1] + 2 * dy)
    c = (
        (b[0] + d[0]) / 2 - np.sqrt(3) * (b[1] - d[1]) / 2,
        (b[1] + d[1]) / 2 + np.sqrt(3) * (b[0] - d[0]) / 2
    )

    koch_curve(ax, a, b, order - 1)
    koch_curve(ax, b, c, order - 1)
    koch_curve(ax, c, d, order - 1)
    koch_curve(ax, d, p2, order - 1)

def draw_koch_square(order, size=1.0):
    fig, ax = plt.subplots()
    origin = (0, 0)
    p1 = origin
    p2 = (origin[0] + size, origin[1])
    p3 = (origin[0] + size, origin[1] + size)
    p4 = (origin[0], origin[1] + size)

    # Внутрішнє застосування: на кожній стороні рекурсивно
    koch_curve(ax, p1, p2, order)  # нижня сторона
    koch_curve(ax, p2, p3, order)  # права сторона
    koch_curve(ax, p3, p4, order)  # верхня сторона
    koch_curve(ax, p4, p1, order)  # ліва сторона

    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

draw_koch_square(order=3)
