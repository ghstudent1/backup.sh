# backup.sh
in the backup.sh file you will find the diffirent instrictions to  create a buchup dir and move it in case of removing of the original data :
1-Create acompressed directory of the original data in /tmp dir
2-Move to /tmp and decompress the data
3-Check if the origianal directory exist or not if not restore the data using the rsync cmd to move the bachup directory from the /tmp to original  path

ps: this script is scheduled by using a crontab command that execute the bachup.sh file evrey 1 minite (* * * * * ./backup.sh(typed in crontab -e ubunto version) )and compres the original  directory with the updated data to still up to date then move it to the /tmp and decompress it and check if the original dir exist or not in the first case nothing to do still rexecute and create new compressed dir every time the script was run with the updated data in the athercase (original dir removed) it will restore the data .


#bash.py
the sme scripte using python language 
ps:scheduled using crontab by runing the code from the virtual envirement (* * * * * ./venv/bin/python backup.py)
