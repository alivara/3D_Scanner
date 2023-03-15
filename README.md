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

### **Dependencies**

```
Open3D v0.13.0 or later
numpy
matplotlib
```
---

#### **Functions**

---

    main_image(pcd): This function takes a point cloud object as input and crops it based on its bounding box. It then visualizes the cropped point cloud using Open3D.

    crop_img(pcd): This function takes a point cloud object as input and crops it based on predefined values for x, y, and z dimensions. It then returns the cropped point cloud object.

    compare(pcd1, pcd2, visual = False): This function takes two point cloud objects as input and crops them based on predefined values for x, y, and z dimensions. It then changes the color of each point cloud and visualizes them side by side using Open3D. The visual argument can be set to True to display the visualization.

    compare_2(pc_1,pc_2): This function takes two point cloud objects as input and removes non-finite points, duplicates, and normalizes the normals of the point clouds. It then computes the distances of each point in pc_1 to the closest point in pc_2 and plots the distances using a line plot, a box plot, and a histogram.


#### **Data**

---

Data in this project are images which classify into two groups:

* Neg_images: which have been taken from other repositories.
* Pos_images: which are taken from the user and stored in:

  ```
  /opencv_workspace/haarclass/images/pos
  
  ```

#### Theory

---

[Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning-based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

[Here we will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. For this, Haar features shown in the below image are used. They are just like our convolutional kernel. Each feature is a single value obtained by subtracting the sum of pixels under the white rectangle from the sum of pixels under the black rectangle.](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

#### XML Files

---

The aim of this project is by getting the positive images and minimum samples we train the Haarclass and the output is an XML file that we will use to detect the objects.

#### VEC Files

---

The ".vec" files are the output of opencv_createsamples and the after merging them we will use them in training.

#### Python

---

There are three python codes:

* *clean.py: this code is for cleaning Negative images manually.*
* *main_code.py: This code is the main code that you need to run for starting the program.*
* *showtime.py: This code is for testing the XML files which is the output of the training*

#### Environment

---

The picture below is a sample of directories in the server and you can see how the data and files have been managed.

* *VEC_file: all the ".vec" have been stored here.*
  * *Merged_VEC: the final merged ".vec" has been stored here.*
* *images: all the images have been stored here.*
* *pos: folder for positive images.*
* *neg: folder for negative images.*
* *images_data*
  * *data: XML files will be stored here.*
  * *image_i: based on the number of positive images we have in this folder.*
    * *info: samples of the "i"th image will store here.*
* *py_codes: as mentioned before.*
  * *clean.py*
  * *main_code.py*
  * *showtime.py*

![Tree of directories.png](Data/Tree%20of%20directories.png?fileId=288168#mimetype=image%2Fpng&hasPreview=true)

#### **Tutorial**

---

Step by step knowing how to use this program: "How to run the software".

1. Docker image

   ---

   We have run this program on a container and committed an image from this program, which can be pulled also from the docker hub (in private).
   1. the first is to run the image and create a container.

      Image repository is: "alivara/ubuntu18-opencv34-python38:Final"

   ```
   docker run -t -d --name <name for container> alivara/ubuntu18-opencv34-python38:Final
   ```

   ```
   docker ps -a
   ```

   Finding the docker container id from the list and use it below:

   ```
   docker exec -it <container id> /bin/sh
   ```

   ```
   #sudo -i
   root@<container id>:~#cd ..
   root@<container id>:# cd /opencv_workspace/haarclass/ 
   ```

   in the final directory, all the related files are stored there. 2. Now you should copy the positive images to the directory of positive images.

   ```
   docker cp <local server> <docker container id>:/opencv_workspace/haarclass/images/pos
   ```
2. Python

   ---

   After copying the positive images we will need to run the python code to start the program.

   ```
   root@<container id>:# cd /opencv_workspace/haarclass/py_codes
   ```
   1. *clean.py: use if needed.*
   2. *main_code.py: This code has been written in the most automation plan, which means if you use the "default" mode it will run all the programs automatically, and also there is a "customized" mode in the program which means if you need you can change the configuration of "opencv_createsamples" and "opencv_traincascade" and the sized for resizing the positive and negative images.*
   3. *showtime.py: use when the training is finished and get the XML file to this.*

      \*\*For running the program after copy the positive images just run:

      ```
      root@<container id>:# cd /opencv_workspace/haarclass/
      root@<container id>:/opencv_workspace/haarclass#python3 main_code.py
      ```

      \*\* Do not run the python file in the py_codes path \*\*
3. XML file

   ---

   The XML files are stored in the:

   ```
   root@<container id>:# cd /opencv_workspace/haarclass/images_data/data
   ```

   you can give this path to the "showtime.py" to test the XML file which has been created from training.

#### Future Studies

---

For future studies, we are trying to find the optimal parameter for the training and the number of samples.

#### 

### 
