#!bin/bash
# program:
# 	use funtion to repeat inform
# history:
# 2016/04/27

function printit (){
	echo -n "your chioce is "
}

echo "this program will print your chioce"
case $1 in
	"one")
		printit; echo $1 | tr 'a-z' 'A-Z'
		;;
	"two")
		printit; echo $1 | tr 'a-z' 'A-Z'
		;;
	"three")
		printit; echo $1 | tr 'a-z' 'A-Z'
		;;
	*)
		echo "usage $0 {one|two|three}"
		;;
esac
