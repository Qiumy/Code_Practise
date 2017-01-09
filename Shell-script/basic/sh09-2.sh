#!bin/bash
# program:
# 	show hello from $1 by using case  esac
# history:
# 2016/04/27

case $1 in
	"hello" )
		echo "Hello, how are you?"
		;;
	"")
		echo "you must input parameters, ex> {$0 someword}"
		;;
	*)
		echo "usage $0 {hello}"
		;;
esac
