# Calibration Simulator
Repository including Gazebo models, plugins and worlds to test calibration algorithms for several sensors (Currently only Bumblebee XB3 and Velodyne VLP-16 are supported).

![gazebo screenshot](screenshots/velo2cam_calibration_setup.png)

# Gazebo models (need to be moved to ~/.gazebo/models/)
* Bumblebee XB3 Camera (Left - center only)
* Velodyne VLP-16 (Based on https://bitbucket.org/DataspeedInc/velodyne_simulator)
* Calibration pattern with wood (maple) texture

# Gazebo plugins (compilation of the pkg installs the lib in the proper directory)
* Velodyne plugin providing PointCloud2 with same structure as driver (x, y, z, intensity, ring) and simulated Gaussian noise. (From https://bitbucket.org/DataspeedInc/velodyne_simulator)

# Known Issues
* Gazebo can take up to 30 seconds to load the VLP-16 pluggin, 60 seconds for the HDL-32E
* Gazebo cannot maintain 10Hz with large pointclouds
    * Solution: User can reduce number of points in urdf

# Example Gazebo Calibration Scenario
```roslaunch calibration_simulator calibration_simulator.launch```
