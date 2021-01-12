import numpy as np

# Target keypoints (in target ref system)
c1_target = np.array([[0, -0.25, 0.2, 1]])
c2_target = np.array([[0, 0.25, 0.2, 1]])
c3_target = np.array([[0, 0.25, -0.2, 1]])
c4_target = np.array([[0, -0.25, -0.2, 1]])

center_target = np.array([[0, 0, 0, 1]])

# Calibration target TF
Tc = np.array([[2, 0, 1.5]])
Rc = np.array([[-1, 0, 0],[0, -1, 0],[0, 0, 1]])
RTc = np.hstack((Rc,Tc.T))
RTc = np.vstack((RTc, np.array([[0,0,0,1]])))

# Sensor TF
#Ts = np.array([[0, 0, 2]]) # P1
#Rs = np.array([[1.0, 0.0, 0.0],[0.0,  1.,  0.],[0, 0., 1.]]) # P1

#Ts = np.array([[-4.5, 2, 1.5]]) # P2
#Rs = np.array([[1.0, 0.0, 0.0],[0.0,  0.6967067,  0.7173561],[0, -0.7173561, 0.6967067]]) # P2

#Ts = np.array([[-1.5, 0.5, 2.5]]) # P3
#Rs = np.array([[0.9800666, 0.0, 0.1986693],[0.0,  1.,  0],[-0.1986693, 0, 0.9800666]]) # P3

Ts = np.array([[-3, -2, 2]]) # P4
Rs = np.array([[0.9210610, -0.3894183,  0.0000000],[0.3894183,  0.9210610,  0.0000000],[0, 0, 1]]) # P4

RTs = np.hstack((Rs,Ts.T))
RTs = np.vstack((RTs, np.array([[0,0,0,1]])))

# Target keypoints transformation
c1_world = np.dot(RTc, c1_target.T)
c2_world = np.dot(RTc, c2_target.T)
c3_world = np.dot(RTc, c3_target.T)
c4_world = np.dot(RTc, c4_target.T)
target_center_world = np.dot(RTc, center_target.T)
c1_lidar = np.dot(np.linalg.inv(RTs), c1_world)
c2_lidar = np.dot(np.linalg.inv(RTs), c2_world)
c3_lidar = np.dot(np.linalg.inv(RTs), c3_world)
c4_lidar = np.dot(np.linalg.inv(RTs), c4_world)
target_center_lidar = np.dot(np.linalg.inv(RTs), target_center_world)

print('LiDAR points')
print('c1 ', c1_lidar.T)
print('c2 ', c2_lidar.T)
print('c3 ', c3_lidar.T)
print('c4 ', c4_lidar.T)
print('target ', target_center_lidar.T)


# If sensor is a camera, perform axis rotation

c1_camera = np.ones(4)
c1_camera[0]= -c1_lidar[1,0]
c1_camera[1]= -c1_lidar[2,0]
c1_camera[2]= c1_lidar[0,0]
c2_camera = np.ones(4)
c2_camera[0]= -c2_lidar[1,0]
c2_camera[1]= -c2_lidar[2,0]
c2_camera[2]= c2_lidar[0,0]
c3_camera = np.ones(4)
c3_camera[0]= -c3_lidar[1,0]
c3_camera[1]= -c3_lidar[2,0]
c3_camera[2]= c3_lidar[0,0]
c4_camera = np.ones(4)
c4_camera[0]= -c4_lidar[1,0]
c4_camera[1]= -c4_lidar[2,0]
c4_camera[2]= c4_lidar[0,0]


target_center_camera = np.ones(4)
target_center_camera[0]= -target_center_lidar[1,0]
target_center_camera[1]= -target_center_lidar[2,0]
target_center_camera[2]= target_center_lidar[0,0]

print('Camera points')
print('c1 ', c1_camera)
print('c2 ', c2_camera)
print('c3 ', c3_camera)
print('c4 ', c4_camera)
print('target ', target_center_camera.T)
