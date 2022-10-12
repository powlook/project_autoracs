# Project AutoRACS

This ROS package provides the launch, world, and model files to
load the simple lake terrain into Gazebo and spawn 3 turtlebots onto the terrain.


## Installation

1. Clone this repository into the `src` in your ROS1 workspace. Assuming that you are using the ubuntu16 VM that we
   all spawn from

        $ cd /home/ubuntu16/catkin_ws/src/
        $ git clone git@github.com:powlook/project_autoracs.git

2. Add these lines to your .bashrc file in the home directory

	export TURTLEBOT3_MODEL=waffle_pi
	export GAZEBO_MODEL_PATH=/home/ubuntu16/catkin_ws/src/project_autoracs/models:$GAZEBO_MODEL_PATH
	source /opt/ros/kinetic/setup.bash
	source catkin_ws/devel/setup.sh

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
