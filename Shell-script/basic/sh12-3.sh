#!bin/bash
# program:
# 	use funtion to repeat information
# history:
# 2016/04/27

function printit (){
	echo "your chioce is $1"
}

echo "this program will print your chioce"
case $1 in
	"one")
		printit 1
		;;
	"two")
		printit 2
		;;
	"three")
	        printit 3
		;;
	*)
		echo "usage $0 {one|two|three}"
		;;
esac
