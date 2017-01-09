#!bin/bash
# program:
# 	check $1 is equal to "hello"
# history:
# 2016/04/27  minyi first release

if [ "$1" == "hello" ]; then
	echo "Hello, how are you ?"
elif [ "$1" == "" ]; then
	echo "you must input parameters, ex> {$0 someword}"
else
	echo "the only parameter is 'hello', ex> {$0 hello}"
fi
