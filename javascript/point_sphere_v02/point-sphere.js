import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';


function normalizeArray(arr) {
    const minValue = Math.min(...arr);
    const maxValue = Math.max(...arr);
    return arr.map(value => (value - minValue) / (maxValue - minValue));
  }

  function great_circle_distance(a, b) {
    const R = 1; // Radius of the sphere
    const lat1 = Math.asin(a[2] / R);
    const lon1 = Math.atan2(a[1], a[0]);
    const lat2 = Math.asin(b[2] / R);
    const lon2 = Math.atan2(b[1], b[0]);
  
    const dLat = lat2 - lat1;
    const dLon = lon2 - lon1;
  
    const x = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(lat1) * Math.cos(lat2) *
              Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(x), Math.sqrt(1 - x));
  
    return R * c;
  }
  
function heatmap(points, k = 5) {
    const distances = points.map((point, i) => {
      const otherPoints = points.slice(0, i).concat(points.slice(i + 1));
      const pointDistances = otherPoints.map(otherPoint => great_circle_distance(point, otherPoint));
      return pointDistances.sort((a, b) => a - b).slice(0, k);
    });
  
    const meanDistances = distances.map(arr => arr.reduce((a, b) => a + b) / k);
    return meanDistances;
}
  
  


// Add this function to generate random points on the surface of the sphere
function sphere_point_picking_marsaglia(n) {
  const points = [];
  while (points.length < n) {
    const x1 = Math.random() * 2 - 1;
    const x2 = Math.random() * 2 - 1;
    if (x1 ** 2 + x2 ** 2 < 1) {
      const x = 2 * x1 * Math.sqrt(1 - x1 ** 2 - x2 ** 2);
      const y = 2 * x2 * Math.sqrt(1 - x1 ** 2 - x2 ** 2);
      const z = 1 - 2 * (x1 ** 2 + x2 ** 2);
      points.push([x, y, z]);
    }
  }
  return points;
}

const container = document.getElementById('heatmapContainer');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, container.offsetWidth / container.offsetHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize(container.offsetWidth, container.offsetHeight);
container.appendChild(renderer.domElement);

const geometry = new THREE.SphereGeometry(1, 32, 32);
const material = new THREE.MeshPhongMaterial({ color: 0xffffff, wireframe: true });
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

const light = new THREE.PointLight(0xffffff, 1, 0);
light.position.set(10, 10, 10);
scene.add(light);

camera.position.z = 3;

function visualize(points, heatmapValues) {
  for (let i = 0; i < points.length; i++) {
    const x = points[i][0];
    const y = points[i][1];
    const z = points[i][2];
    const color = evaluate_cmap( heatmapValues[i], 'coolwarm', true);
    const material = new THREE.MeshBasicMaterial({ color: `rgb(${color[0]}, ${color[1]}, ${color[2]})` });
    const geometry = new THREE.SphereGeometry(0.02);
    const point = new THREE.Mesh(geometry, material);
    point.position.set(x, y, z);
    scene.add(point);
  }
}

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.1;
controls.screenSpacePanning = false;
controls.minDistance = 1.5;
controls.maxDistance = 10;
controls.maxPolarAngle = Math.PI;

function animate() {
  requestAnimationFrame(animate);
  controls.update(); // Add this line to update controls on each frame
  renderer.render(scene, camera);
}

animate();

const n_points = 1000;
const points = sphere_point_picking_marsaglia(n_points);
const heatmapValues = heatmap(points);
const normalizedHeatmapValues = normalizeArray(heatmapValues);
visualize(points, normalizedHeatmapValues);


