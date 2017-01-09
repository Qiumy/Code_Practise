#!bin/bash
# program:
# 	thid script only accept the following parameter: one, two, three
# history:
# 2016/04/27 minyi first

echo "this program will your selection"
# read -p "input your choice: " choice
# case $choice in
case $1 in
	"one")
		echo "your chioce is one"
		;;
	"two")
		echo "your chioce is two"
		;;
	
	"three")
		echo "your chioce is three"
		;;
	*)
		echo "usage $0 {one|two|three}"
		;;
esac
