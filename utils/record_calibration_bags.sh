#!/usr/bin/env bash
if [ "$#" -lt 4 ]; then
	echo "Illegal number of parameters. Required: <folder> <p#> <bag_count> <noise> (<noise>) (<noise>)"
	exit
fi

#POSE="p1"
#BAGCOUNT=3
#NOISES=("ideal" "real" "noise") 
#FOLDER="/home/beltransen/ros_ws/src/velo2cam_gazebo/velo2cam_gazebo/launch/magazine/single_sensor/*"
#roscore &
FOLDER=$1
POSE=$2
BAGCOUNT=$3
NOISES=($4)
NOISES+=($5)
NOISES+=($6)

for sensor in $FOLDER/*; 
do
	MODALITY="$(basename "${sensor}")"
	for experiment in $sensor/*;
	do
		if [[ $experiment == *$POSE\_* ]]; then
			for n in ${NOISES[@]}; 
			do 
				if echo "$experiment" | grep -q "$n"; then
					# If bag with last number exists, skip experiment
					LASTBAG="$(basename -s .launch "${experiment}")"_$(expr $BAGCOUNT - 1)
					
					if [ -f "$HOME/.ros/$LASTBAG.bag" ]; then
						echo "$(basename -s .launch "${experiment}")"" already done. Skipping."
						continue
					fi
					roslaunch $experiment &
					sleep 30
					for i in $(seq 0 $(expr $BAGCOUNT - 1)); 
					do
						BAGNAME="$(basename -s .launch "${experiment}")"_$i
						if ! [ -f "$HOME/.ros/$BAGNAME.bag" ]; then
						    roslaunch velo2cam_gazebo record_$MODALITY.launch bag_name:=$BAGNAME
						fi
					done
					killall roslaunch
					sleep 30
				fi
			done
		fi
	done
	
done

#killall roscore
