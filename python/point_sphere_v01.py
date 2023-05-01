'''
Version 1 - Uniformly Random Selection of Points on the Surface of a Unit Sphere 
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sphere_point_picking_uv(n):
    u = np.random.rand(n)
    v = np.random.rand(n)
    theta = 2 * np.pi * u
    phi = np.arccos(2 * v - 1)
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    return np.stack((x, y, z), axis=1)

def sphere_point_picking_marsaglia(n):
    points = []
    while len(points) < n:
        x1, x2 = np.random.uniform(-1, 1, size=2)
        if x1**2 + x2**2 < 1:
            x = 2 * x1 * np.sqrt(1 - x1**2 - x2**2)
            y = 2 * x2 * np.sqrt(1 - x1**2 - x2**2)
            z = 1 - 2 * (x1**2 + x2**2)
            points.append([x, y, z])
    return np.array(points)

def sphere_point_picking_cook(n):
    points = []
    while len(points) < n:
        x0, x1, x2, x3 = np.random.uniform(-1, 1, size=4)
        if x0**2 + x1**2 + x2**2 + x3**2 < 1:
            norm = np.sqrt(x0**2 + x1**2 + x2**2 + x3**2)
            x = (2 * (x1*x3 + x0*x2)) / norm
            y = (2 * (x2*x3 - x0*x1)) / norm
            z = (x0**2 + x3**2 - x1**2 - x2**2) / norm
            points.append([x, y, z])
    return np.array(points)

def sphere_point_picking_gaussian(n):
    x = np.random.normal(size=n)
    y = np.random.normal(size=n)
    z = np.random.normal(size=n)
    norm = np.sqrt(x**2 + y**2 + z**2)
    x /= norm
    y /= norm
    z /= norm
    return np.stack((x, y, z), axis=1)



def main():
    # Generate 1000 random points on the surface of a unit sphere
    points = sphere_point_picking_uv(1000)

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=2)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    plt.show()


if __name__ == "__main__":
    main()

