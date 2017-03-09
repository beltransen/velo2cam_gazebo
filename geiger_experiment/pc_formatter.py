#!/usr/bin/env python
import sys
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField

busy = False

def callback(data):
	global busy
	if busy == False:
		busy = True
		print "# points %s" % data.width
		f = open('pointcloud.txt', 'w')
		#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.header.stamp)
		for point in pc2.read_points(data, skip_nans=True):
				pt_x = point[0]
				pt_y = point[1]
				pt_z = point[2]
				f.write("%s %s %s\n" % (pt_x, pt_y, pt_z))
		print "ENd of pointcloud"
	
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("velodyne_points", PointCloud2, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
