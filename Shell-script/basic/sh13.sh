#!bin/bash
# program:
# 	repeat question until correct answer
# history:
# 2016/04/27 minyi first
while [ "$yn" != "yes" -a "$yn" != "YES" ]
do
	read -p "please input yes/YES to stop this program: " yn
done
echo "ok! your input is the correct answer"

