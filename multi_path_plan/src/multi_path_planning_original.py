#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

global position_tb3_0_x
global position_tb3_0_y
global position_tb3_1_x
global position_tb3_1_y
global goal_publisher0
global goal_publisher1

goal_publisher0 = rospy.Publisher("tb3_0/move_base_simple/goal", PoseStamped, queue_size=5)
goal_publisher1 = rospy.Publisher("tb3_1/move_base_simple/goal", PoseStamped, queue_size=5)

def callback0(msg):
  #print("Executing callback0")

  global position_tb3_0_x
  global position_tb3_0_y

  position_tb3_0 = msg.pose.pose.position
  quat_tb3_0 = msg.pose.pose.orientation
  position_tb3_0_x = position_tb3_0.x
  position_tb3_0_y = position_tb3_0.y

def callback1(msg):
  #print("Executing callback1")

  global position_tb3_1_x
  global position_tb3_1_y

  position_tb3_1 = msg.pose.pose.position
  quat_tb3_1 = msg.pose.pose.orientation
  position_tb3_1_x = position_tb3_1.x
  position_tb3_1_y = position_tb3_1.y
 
def callback(goal):
  #print("Executing callback")
  print(goal)
  global position_tb3_0_x
  global position_tb3_0_y
  global position_tb3_1_x
  global position_tb3_1_y
  global goal_publisher0
  global goal_publisher1

  goal_position_x = goal.pose.position.x
  goal_position_y = goal.pose.position.y

  x_distance_tb3_0 = goal_position_x-position_tb3_0_x
  y_distance_tb3_0 = goal_position_y-position_tb3_0_y
  total_distance_tb3_0 = math.sqrt((x_distance_tb3_0**2)+(y_distance_tb3_0**2))

  print("tb3_0 distance:",total_distance_tb3_0)

  x_distance_tb3_1 = goal_position_x-position_tb3_1_x
  y_distance_tb3_1 = goal_position_y-position_tb3_1_y
  total_distance_tb3_1 = math.sqrt((x_distance_tb3_1**2)+(y_distance_tb3_1**2))

  print("tb3_1 distance:",total_distance_tb3_1)
  
  if (total_distance_tb3_1>total_distance_tb3_0):
    goal_publisher0.publish(goal)
    print("tb3_0 on the way")

  elif (total_distance_tb3_1<total_distance_tb3_0):
    goal_publisher1.publish(goal)
    print("tb3_1 on the way")

if __name__ == "__main__":

  rospy.init_node("test2")

  odom_sub_tb3_0 = rospy.Subscriber('/tb3_0/odom', Odometry, callback0)
  odom_sub_tb3_1 = rospy.Subscriber('/tb3_1/odom', Odometry, callback1) 

  goal_sub = rospy.Subscriber("/move_base_simple/goal", PoseStamped, callback)
  print("Code correctly executed, rospy.spin started")

  rospy.spin()
