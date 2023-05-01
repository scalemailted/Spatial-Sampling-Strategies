# 3D Spatial Sampling Strategies 

---

## Project Objectives
Generate uniformly random samples (cones) with random orientation on the surface of a unit sphere, as illustrated below:

![Sphere Sampling](./assets/sphere-sampling-objective.png)

---

## Motivations
Random sampling is a crucial technique in various fields, including robotics and path planning. In many problems, the high dimensionality of the configuration space (c-space) results in combinatorial explosion, making it challenging to find optimal solutions. Random sampling may provide a near-optimal or good enough solution faster and more efficiently than an exhaustive search.

In 3D space, orientation exploration is represented by a sphere. The random orientation of a cone represents a second degree of orientation consideration, i.e., the orientation of both parent and child objects. The distribution of random samples may vary for each problem domain, such as uniform, Gaussian, or power-law. In this instance, we need to ensure the random sample is uniform across the action space to obtain a representative sample of the space. Therefore, generating uniformly random samples on the surface of a unit sphere with random orientation is an effective approach to efficiently explore orientation space.

---

## Approach
 Marsaglia's method is used to ensure a uniform distribution of points on the surface of a unit sphere. This method involves selecting random points in 3D space and rejecting points that fall outside the sphere. This approach is simple, efficient, and effective for generating uniformly distributed points on a sphere. 
 
 The next step is to select a random orientation of the cone. This can be done by generating three random Euler angles for rotation. The Euler angles determine the orientation of the cone with respect to the x, y, and z-axes. By randomly selecting these angles, we can generate a random orientation of the cone. The use of Euler angles provides an intuitive and straightforward representation of rotations, making it an ideal choice for our project.

---

## Key Features
- Uniform selection of random points on the surface of a sphere (rotation from surface)
- Uniform random orientation of a cone (rotation from origin)
- Implement in CoppeliaSim with Python
- Implement in Matplotlib with Python
- Implement as Web Application with JavaScript 
- Visualization of point density using a heatmap to illustrate uniform distrbution.

---

## Algorithmic Overview:

### 3D Space-fixed rotation: Uniform Random Points on Sphere Surface

Using the Marsaglia method, the following steps generate a uniformly random point on the surface of a unit sphere:

1. Generate two random numbers `x1` and `x2`, uniformly distributed between `-1` and `1`.
2. Check if the point (x1, x2) falls within the unit circle: `x1^2 + x2^2 < 1`. If not, repeat step 1.
3. Compute the Cartesian coordinates of the point on the sphere using the following equations:


```
   x = 2 * x1 * sqrt(1 - x1^2 - x2^2)
   y = 2 * x2 * sqrt(1 - x1^2 - x2^2)
   z = 1 - 2 * (x1^2 + x2^2)
```
   
This procedure ensures a uniform distribution of points across the surface of the sphere.

### 3D Body-fixed rotation: Uniform Random Orientations

To generate a uniform random orientation, the following steps use Euler angles to represent the rotation around the x-axis, y-axis, and z-axis:

1. Generate three random numbers `alpha`, `beta`, and `gamma`, each uniformly distributed between 0 and 2π radians.
2. Use these Euler angles to represent the rotations around the x-axis (`alpha`), y-axis (`beta`), and z-axis (`gamma`).
3. Apply the rotations sequentially to obtain the final orientation of the cone.

By uniformly sampling each angle, every possible orientation on the surface of the sphere has an equal probability of being selected, guaranteeing a uniform distribution of orientations.

---

## Implementation: 

### *CoppeliaSim* 
![Demo: CoppeliaSim](./assets/coppeliasim-sphere-sample.gif)


### *Python*
![Demo: Python](./assets/py-sphere-sample.gif)



### *JavaScript*
[![Demo: JavaScript](./assets/js-sphere-sample.gif)](https://scalemailted.github.io/Basic-Motion-Planning/WebApp/)

---

## Project Hierarchy 
- 📁 assets/
    + contains all images in readme documentation
- 📁 coppeliaSim/
    + 📁 scenes/
        - contains CoppeliaSim scenes (.tt)
    + 📁 scripts/
        - contains associated Python scripts from the scene
- 📁 python/
    + contains code for standalone Python app
- 📁 javascript/
    + contains code for standalone JavaScript app