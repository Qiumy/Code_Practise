#!bin/bash
# program:
# 	try do calculate 1+2..+${your_input}
# history:
# 2016/04/27 minyi first
read -p "please input a number, i will count for 1+2+..+your_input: " nu
s=0
for (( i=1; i<=$nu; i=i+1 ))
do
	s=$(($s+$i))
done
echo "the result of '1+2+3+..+$nu' is ==> $s"
