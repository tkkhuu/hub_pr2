# hub_pr2
Code for detecting signal from the sensors using Raspberry Pi and ROS, instructions on running the code:

	1) Running the master:
		- Log into the master machine with ROS, source the setup.bash file
		- Run "export ROS_MASTER_URI=http://<IP address of this machine>:11311
		- Run "export ROS_IP=<IP address of this machine"
		- run "roscore"
		
		- Open a new terminal, source the setup.bash file
		- Create a ROS package using "roscreate-pkg hub_pr2 roscpp rospy std_msgs"
		- Run "rosmake hub_pr2"
		- Run "roscd hub_pr2"
		- Run "mkdir scripts"
		- Run "cd scripts"
		- Copy the file get_signal.py into this directory, make it execuateble by running "chmod +x get_signal.py"
		- Run "export ROS_MASTER_URI=http://<IP address of this machine>:11311
		- Run "export ROS_IP=<IP address of this machine"
		- Run "rosrun hub_pr2 get_signal.py"
		
	2) Running the Raspberry Pi
		- Log into the Raspberry Pi as root using "sudo su"
		- Source the setup.bash file, for the Pi used for the lab, it should be "source ~/tri_ws/setup.bash"
		- Run "export ROS_MASTER_URI=http://<IP address of the master machine>:11311
		- Run "export ROS_IP=<IP address of the Pi"
		- The script signal_detector.py should already be in the package hub_pr2, so we only have to run "rosrun hub_pr2 signal_detector.py"

		
