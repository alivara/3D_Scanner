
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.gridspec import GridSpec

device = o3d.core.Device("CPU:0")
dtype = o3d.core.float32

def main_image(pcd):
    # Get bounding box
    bbox = pcd.get_axis_aligned_bounding_box()

    # Get max and min bounds of bounding box
    min_bound = bbox.get_min_bound()
    max_bound = bbox.get_max_bound()
    print(f'max bounfing: {max_bound}\nmin bounding: {min_bound}')

    # Calculate middle of bounding box **half
    middle = (max_bound + min_bound) / 2.0

    # Define cropping distance from middle
    crop_distance = 1000.0

    # Create new bounding box around middle of original bounding box
    cropped_bbox = o3d.geometry.AxisAlignedBoundingBox(
        min_bound=[middle[0]-crop_distance, middle[1]-crop_distance, middle[2]-crop_distance],
        max_bound=[middle[0]+crop_distance, middle[1]+crop_distance, middle[2]+crop_distance])

    # Crop point cloud using new bounding box
    cropped_pcd = pcd.crop(cropped_bbox)

    # Visualize cropped point cloud
    o3d.visualization.draw_geometries([cropped_pcd]) # main image

def crop_img(pcd):
    # based on value afte transform
    x_min, x_max = -300, 600.0   # Set the minimum and maximum x values for the cropping region
    y_min, y_max = -50.0, 250.0  # Set the minimum and maximum y values for the cropping region
    z_min, z_max = -3242, 0.0 # Set the minimum and maximum z values for the cropping region
    
    # Crop the point cloud
    crop_box = o3d.geometry.AxisAlignedBoundingBox(min_bound=[x_min, y_min, z_min], max_bound=[x_max, y_max, z_max])
    cropped_pcd = pcd.crop(crop_box)
    
    # Visualize the cropped point cloud
    # o3d.visualization.draw_geometries([cropped_pcd])
    return cropped_pcd


def compare(pcd1,pcd2,visual = False):
    # ROI bounding
    x_min, x_max = -400, 200.0   
    y_min, y_max = -250.0, 150.0  
    z_min, z_max = 0.0, 2700.0 
    
    # Crop the point cloud (boundries has been defined on the first part of program)
    crop_box = o3d.geometry.AxisAlignedBoundingBox(min_bound=[x_min, y_min, z_min], max_bound=[x_max, y_max, z_max])
    cropped_pcd1 = pcd1.crop(crop_box)
    cropped_pcd2 = pcd2.crop(crop_box)
    
    # change color
    cropped_pcd1.paint_uniform_color([0,0,1])
    cropped_pcd2.paint_uniform_color([0.5,0.5,0])
    
    if visual == True:
        o3d.visualization.draw_geometries([cropped_pcd1,cropped_pcd2])
    
    return cropped_pcd1,cropped_pcd2

def compare_2(pc_1,pc_2):
    pc_1.remove_non_finite_points()
    pc_1.remove_duplicated_points()
    pc_1.normalize_normals()
    pc_2.remove_non_finite_points()
    pc_2.remove_duplicated_points()
    pc_2.normalize_normals()
    pc_1.paint_uniform_color([0,0,1])
    pc_2.paint_uniform_color([0.5,0.5,0])
    # o3d.visualization.draw_geometries([pc_1,pc_2])
    # Calculate distances of pc_1 to pc_2. 
    dist_pc1_pc2 = pc_1.compute_point_cloud_distance(pc_2)
    # acess the data
    dist_pc1_pc2 = np.asarray(dist_pc1_pc2)
    # define x,y,z
    x = np.asarray(pc_1.points,dtype='float16')[:, 0]
    y = np.asarray(pc_1.points,dtype='float16')[:, 1]
    ## Calculate distances of pc_1 to pc_2 as z
    dist_pc1_pc2 = pc_1.compute_point_cloud_distance(pc_2)
    ## dist_pc1_pc2 is an Open3d object, we need to convert it to a numpy array to 
    dist_pc1_pc2 = np.asarray(dist_pc1_pc2)
    z = dist_pc1_pc2
    
    # plot
    fig = plt.figure(figsize=(20, 10))
    gs = GridSpec(nrows=6, ncols=7,hspace=0.6,wspace=0.5)
    ## Line plot
    ax0 = fig.add_subplot(gs[0:2, 0:2])
    ax0.plot(z)
    ax0.set_title('Distance line Plot',fontsize=10)  
    
    ## Box plot
    ax1 = fig.add_subplot(gs[2:4, 0:2])
    box_data = ax1.boxplot(z)
    ax1.set_title('Distance Box Plot',fontsize=10)
    
    ## Hostogram plot
    ax2 = fig.add_subplot(gs[4:6, 0:2])
    ax2.hist(z,alpha=0.5, bins = 1000)
    ax2.set_title('Distance Hostogram Plot',fontsize=10)  
    
    ## Heatmap plot
    ax3 = fig.add_subplot(gs[1:5, 2:])
    T = [item.get_ydata()[1] for item in box_data['fliers']][0]
    z[z > T] = T ### add treshold for z
    gridsize=500
    pcm = ax3.hexbin(x, y, C=z, gridsize=gridsize, cmap=cm.jet, bins=None)
    ax3.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(pcm, ax=ax3)
    ax3.set_title('Distance Heatmap (Y inverted) -- T = '+str(format(T, '.3f'))+' -- gridsize = '+str(gridsize),fontsize=10)  
    plt.show()
    
    # visualize data
    o3d.visualization.draw_geometries([pc_1,pc_2]) # show again

# number of valid data: 1 , 6 , 12, 16, 17, 18, 26, 30, 
pcd1 = o3d.io.read_point_cloud("/home/player/calibration/TOFCamera/scan_0001.ply")
pcd2 = o3d.io.read_point_cloud("/home/player/calibration/TOFCamera/scan_0030.ply")

# o3d.visualization.draw_geometries([pcd1])
T = np.array([[ 1.0, 0.0, 0.0, 0.0],
              [ 0.0, -1.0, 0.0, 0.0],
              [ 0.0, 0.0, -1.0, 0.0],
              [ 0.0, 0.0, 0.0, 1.0]])

pcd1.transform(T)
pcd2.transform(T)

# visualize data before satrting process
pcd1.paint_uniform_color([0,0,1])
pcd2.paint_uniform_color([0.5,0.5,0])
o3d.visualization.draw_geometries([pcd1,pcd2])
# exit()
# main_image()
pcd1_crop = crop_img(pcd1)
# exit()
pcd2_crop = crop_img(pcd2)
# exit()
compare_2(pcd1_crop,pcd2_crop)
# cropped_pcd1,cropped_pcd2 = compare(pcd1,pcd2)
# heatmap_tem(cropped_pcd1,cropped_pcd2)


