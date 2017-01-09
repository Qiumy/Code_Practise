#!bin/bash
# program:
# 	programe shows the script name, parameters
# history:
# 2016/04/26

echo "the script name is   ==> $0"
echo "total parameter number is  ==> $#"
[ "$#" -lt 2 ] && echo "the number of parameter is less than 2, stop here." && exit 0
echo "your whole parameter is  ==> $@"
echo "your 1st parameter is ==> $1"
echo "your 2nd parameter is ==> $2"
