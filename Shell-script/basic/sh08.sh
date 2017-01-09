#!bin/bash
# program:
# 	program shows the effect of shift funtion.
# history:
# 2016/04/16
echo "total parameter number is ==> $#"
echo "your whole parameter is ==> $@"
shift
echo "total parameter number is ==> $#"
echo "your whole parameter is ==> $@"
shift 3
echo "total parameter number is ==> $#"
echo "your whole parameter is ==> $@"

