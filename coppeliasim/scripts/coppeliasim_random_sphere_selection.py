#python
import numpy as np

def sysCall_init():
    create_unit_sphere()
    create_cones_on_sphere(200)  # Create 100 cones on a unit sphere

def sysCall_actuation():
    # put your actuation code here
    pass

def sysCall_sensing():
    # put your sensing code here
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details


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

def create_cones_on_sphere(n, cone_height=0.1, cone_radius=0.1, z_height=1):
    points = sphere_point_picking_marsaglia(n)
    
    for point in points:
        # Create a cone shape
        cone = sim.createPrimitiveShape(sim.primitiveshape_cone, [cone_radius, cone_height, cone_height], 1)
        
        # Set the cone position
        sim.setObjectPosition(cone, -1, [point[0], point[1], point[2]+z_height])
                
        # Get the random Euler angles for rotation
        alpha = np.random.uniform(0, 2* np.pi)
        beta = np.random.uniform(0, 2* np.pi)
        gamma = np.random.uniform(0, 2* np.pi)
        
        #Set the cone's rotation
        sim.setObjectOrientation(cone, -1, [alpha, beta, gamma])
        

def create_unit_sphere(radius=2.0, color=[0, 0, 1], opacity=0.5, z_height=1):
    sphere = sim.createPrimitiveShape(sim.primitiveshape_spheroid, [radius, radius, radius], 1)
    sim.setShapeColor(sphere, None, 0, color)
    sim.setShapeColor(sphere,None,sim.colorcomponent_transparency,[0.5])
    sim.setObjectPosition(sphere,-1,[0.0, 0.0, z_height])
    return sphere
