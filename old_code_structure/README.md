# Project AutoRACS

This ROS package provides the launch, world, and model files to
load the simple lake terrain into Gazebo and spawn 3 turtlebots onto the terrain.


## Installation

1. Clone this repository into the `src` in your ROS1 workspace. Assuming that you are using the ubuntu16 VM that we
   all spawn from

        $ cd /home/ubuntu16/catkin_ws/src/
        $ git clone git@github.com:powlook/project_autoracs.git

2. Add these lines to your .bashrc file in the home directory

	- export TURTLEBOT3_MODEL=waffle_pi
	- export GAZEBO_MODEL_PATH=/home/ubuntu16/catkin_ws/src/project_autoracs/models:$GAZEBO_MODEL_PATH
	- source /opt/ros/kinetic/setup.bash
	- source catkin_ws/devel/setup.sh

3. Move the turtlebot3_simulations folder to the trash folder. (Do not delete first)
   The project_autoracs folders has some dependencies installed which will conflict with turtlebot_simulations

4. Source the ROS system environment and source the Gazebo environment

        $ cd
        $ . /opt/ros/<ROS_DISTRO>/setup.bash
        $ . /usr/share/gazebo/setup.sh

5. Install dependencies and build the package

        $ cd catkin_ws
        $ rosdep install --from-paths src --ignore-src -r -y
        $ catkin_make
   When you catkin_make, check that there are no errors in the make process. Fix the errors even if the catkin_make
   is successful.

6. Open a new terminal and launch the example below

        $ roslaunch project_autoracs multi_robots.launch


At this point, Gazebo should have launched, loaded the simple lake terrain, and
spawned 3 turtlebot3  onto the terrain. A common mistake is to forgot
to source the Gazebo environment in step 2.


## Multiple turtlebots SLAM

1. First, you need to install the ros-kinetic-multirobot-map-merge package (only need to do for the first time)

        $ sudo apt install ros-kinetic-multirobot-map-merge

2. Start the pillar10x10 world (pillar10x10.world) with 2 turtlebots. Utilize the turtlebot3_drive.cpp to navigate the turtlebots.

        $ roslaunch multi_slam robots_multi_moving.launch

3. Subcript to the map topics of both turtlebots and merge the 2 maps

        $ roslaunch multi_slam robots_multi_map_merge.launch

4. Visualize the maps

        $ rosrun rviz rviz -d `rospack find multi_slam`/rviz/robots_multi_slam.rviz

5. Save the map

        $rosrun map_server map_saver -f ~/map/map_filename

## Multiple turtlebots Navigation

1. Launch the global map (after merging) and the pillar10x10.world

        $ roslaunch multi_nav robots_multi_static.launch

2. Launch the navigation node for multiple turtlebots navigation

        $ roslaunch multi_nav robots_multi_navigation.launch

FAQ: 
1. I have issue with map_merge package. Check if the ros-kinetic-multirobot-map-merge already installed.
2. Why initial_pose.py fail? Check the file, make sure it is executable.


