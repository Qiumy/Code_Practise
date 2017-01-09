#!bin/bash
# programe:
# 	user input 2 integer number; program will cross these two number
# history:
# 2016/04/26 minyi first

echo -e "you should input 2 numbers, i will cross them"
read -p "first number: " firstnu
read -p "second number: " secondnu
total=$(($firstnu*$secondnu))
echo -e "\nThe result of $firstnu x $secondnu is ==> $total"

