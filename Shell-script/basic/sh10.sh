#!bin/bash
# program:
# 	using netstat and grep to detect WWW, SHH, FTP, and Mail services.
# history:
# 2016/04/27

echo "now, i will detect your Linux server's services!"
echo -e "the www, ftp, ssh, and mail will be detect! \n"

testing=$(netstat -tuln | grep ":80" )
if [ "$testing" != "" ]; then
	echo "www is running in your system"
fi
  
testing=$(netstat -tuln | grep ":20" )
if [ "$testing" != "" ]; then
	echo "ssh is running in your system"
fi

testing=$(netstat -tuln | grep ":21" )
if [ "$testing" != "" ]; then
	echo "ftp is running in your system"
fi
  
testing=$(netstat -tuln | grep ":25" )
if [ "$testing" != "" ]; then
	echo "mail is running in your system"
fi








