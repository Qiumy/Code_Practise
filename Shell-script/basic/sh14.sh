#!bin/bash
# program:
# 	use loop to calculate "1+2+3+...+100" result
# history:
# 2016/04/27
s=0
i=0
while [ "$i" != "100" ]
do
	i=$(($i+1))
	s=$(($s+$i))
done
echo "the result of '1+2+3+..+100' is ==> $s"
