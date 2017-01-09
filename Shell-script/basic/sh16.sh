#!bin/bash
# program:
# 	use id, finger command to check system account's information
# history:
# 2016/04/27
users=$( cut -d ':' -f1 /etc/passwd)
for username in users
do
	id $username
	finger $username
done
