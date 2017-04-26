# Calibration Simulator
Repository including Gazebo models, plugins and worlds to test calibration algorithms for Lidar and camera sensors.
Currently supported sensors:

* Bumblebee XB3 Camera
* Velodyne VLP-16
* Velodyne HDL-32
* Velodyne HDL-64

![gazebo screenshot](screenshots/velo2cam_calibration_setup.png)

# Gazebo models (need to be moved to ~/.gazebo/models/) so that they can be inserted in Gazebo worlds
Sensors:

* Bumblebee XB3 Camera (Left - center only)
* Velodyne VLP-16 (Based on https://bitbucket.org/DataspeedInc/velodyne_simulator)
* Velodyne HDL-32 (Based on https://bitbucket.org/DataspeedInc/velodyne_simulator)
* Velodyne HDL-64 (Since 3D meshes are not available, those of HDL-32 model are used instead)

Calibration targets:

* Calibration pattern with wood (maple) texture
* Calibration pattern with chessboard texture
* Chessboard planes for Geiger et al. calibration comparison

# Gazebo plugins (compilation of the pkg installs the lib in the proper directory)
* Velodyne plugin providing PointCloud2 with same structure as driver (x, y, z, intensity, ring) and simulated Gaussian noise. (Code from https://bitbucket.org/DataspeedInc/velodyne_simulator, although minor patch for vertical resolution issue is included)

# Known Issues
* Gazebo can take up to 30 seconds to load the VLP-16 pluggin, 60 seconds for the HDL-32E, and much more HDL-64E
* Gazebo cannot maintain 10Hz with large pointclouds
    * Solution: User can reduce number of points in urdf

# Example Gazebo Calibration Scenario
```roslaunch calibration_simulator real_stereoVLP16_trans.launch```