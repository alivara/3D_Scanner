> # **PhoXi_3D_Scanner**
>
> ---
## Table of Contents
---
* *Dependencies*
* *Functions*
* *Usage*
* *Example*
* *License*
---
### **Dependencies**
```
Open3D v0.13.0 or later
numpy
matplotlib
```
---
#### **Functions**
---
- main_image(pcd): This function takes a point cloud object as input and crops it based on its bounding box. It then visualizes the cropped point cloud using Open3D.
- crop_img(pcd): This function takes a point cloud object as input and crops it based on predefined values for x, y, and z dimensions. It then returns the cropped point cloud object.
- compare(pcd1, pcd2, visual = False): This function takes two point cloud objects as input and crops them based on predefined values for x, y, and z dimensions. It then changes the color of each point cloud and visualizes them side by side using Open3D. The visual argument can be set to True to display the visualization.
- compare_2(pc_1,pc_2): This function takes two point cloud objects as input and removes non-finite points, duplicates, and normalizes the normals of the point clouds. It then computes the distances of each point in pc_1 to the closest point in pc_2 and plots the distances using a line plot, a box plot, a histogram, and a Heatmap.
---
#### **Usage**
---
1. Import Open3D, numpy, and matplotlib
  ```
 import open3d as o3d
 import numpy as np
 import matplotlib.pyplot as plt
 from matplotlib import cm
 from matplotlib.gridspec import GridSpec 
  ```
2. Import the functions from the file
  ```
 from point_cloud_processing import main_image, crop_img, compare, compare_2
  ```
3. Load a point cloud object using Open3D and pass it to one of the functions
  ```
    pcd = o3d.io.read_point_cloud("point_cloud.pcd")
    main_image(pcd)

  ```
---
#### **Example**
---
In this test we have tried to crop 3D model based on our ROI and then we have calculated differece of distance by using the compute_point_cloud_distance module. Threshold has been set by using box plot to filter the outliers then by using Heatmap we can find the high deformd area.
![example_result](Examples/Figure_1.png)


---
#### License
---
This code is licensed under the MIT License.

