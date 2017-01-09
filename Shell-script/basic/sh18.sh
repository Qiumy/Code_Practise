#!bin/bash
# program:
# 	user input dir name, i find the permission of files
# history:
# 2016/04/27 minyi first

read -p "please input a directory: " dir
if [ "$dir" == "" -o ! -d "$dir" ]; then
	echo " the $dir is not exist in your system."
	exit 1
fi

filelist=$( ls $dir)
for filename in filelist
do
	perm=""
	test -r "$dir/filename" && perm="$perm readable"
	test -w "$dir/filename" && perm="$perm writable"
	test -x "$dir/filename" && perm="$perm executable"
	echo "the file $dir/filename's permission is $perm"
done
