#!bin/bash
# programe:
#	this program shows the user's choice
# history:
#2016/04/26 minyi first

read -p "please input (Y/N): " yn
[ "$yn" == "Y" -o "$yn" == "y" ] && echo "ok, continue" && exit 0
[ "$yn" == "N" -o "$yn" == "n" ] && echo "oh, interrupt!" && exit 0
echo "i don't know what your choice is " && exit 0
