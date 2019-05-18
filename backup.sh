#!/bin/bash
echo "hello"
echo "you can schedule this script using crontab by typing * * * * * sudo /home/.../eduonix_project/backup.sh(location of the backup.sh file) to execute it evrey minite and check if the data exist or not and restort it in that case "

echo "here is the instriction cycle"
echo "creating compressed backup data of eduonix in/tmp/eduonix_backup.tar "
#c compress z to creat zip v visualise f file to use to createarchive 
tar -czvf /tmp/eduonix_backup.tar ./eduonix
#x extract  z zip  directory v visualise f file to extract from archive
echo "Move to /tmp and decompress the backup"
cd /tmp && tar -xzvf /tmp/eduonix_backup.tar 
echo "check if the directory of data exisit or not "
if [ -d ./eduonix ]
then
        echo "directory exists"
	echo "nothing to do"
else
        echo "directory doesn't exists"
	echo "move the  backup data to the directory using the rsync command"
	rsync -ai /tmp/eduonix ./eduonix
fi


