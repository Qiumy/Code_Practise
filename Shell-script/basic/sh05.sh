#!bin/bash
# program:
#	user input a filename, program will check the follow:
#	1)exist? 2) file/directory? 3) file permissions
# history:
# 2016/04/26 minyi first

echo -e "please input a filename, i will check the filename's type and \
	permission. \n\n"
read -p "input a filename: " filename
test -z $filename && echo "you must input a filename." && exit 0

test ! -e $filename && echo "the filename '$filename' do not exist" && exit 0

test -f $filename && filetype="regulare file"
test -d $filename && filetype="diretory"

test -r $filename && perm="readable"
test -w $filename && perm="$perm writable"
test -x $filename && perm="$perm executable"

echo "the filename: $filename is a $filetype"
echo "and the permission are $perm"
