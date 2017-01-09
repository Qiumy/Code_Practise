#!bin/bash
# program:
# 	using ping command to check the network's PC state
# history:
# 2016/04/27 minyi first
network="192.168.2"
for sitenu in $( seq 1 100)
do
	ping -c 1 -w ${network}.${sitenu} &> /dev/null && result=0 || result=1
	if [ "$result" == 0 ]; then
		echo "server ${network}.${sitenu} is up"
	else
		echo "server ${neteork}.${sitenu} is down"
	fi
done
