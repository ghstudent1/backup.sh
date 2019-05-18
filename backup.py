import os.path
import sys 
from subprocess import Popen ,PIPE

def shell_exec(cmd):
	"""execute the command cmd 
	input:cmd command 
	output cmd execution or error
	"""
	p=Popen(cmd,stdout=PIPE,stderr=PIPE,shell=True)
	out,err=p.communicate()
	exec_code=p.returncode 
	print(out)
	print(err)
	return out,err 


pwd= os.path.dirname(os.path.realpath(__file__))
print("pwd========={}".format(pwd))

print("hello")
print("you can schedule this script using crontab by typing * * * * * sudo /home/.../eduonix_project/backup.sh(location of the backup.sh file) to execute it evrey minite and check if the data exist or not and restort it in that case ")
print("here is the instriction cycle")
print("creating compressed backup data of eduonix in/tmp/eduonix_backup.tar ")

shell_exec("sudo tar -czvf /tmp/eduonix_backup.tar ./eduonix")
print("Move to /tmp and decompress the backup")

shell_exec("sudo tar -xzvf /tmp/eduonix_backup.tar ")
print("check if the directory of data exisit or not ")
pwd= os.path.dirname(os.path.realpath(__file__))
dir_existence=os.path.exists("{}/eduonix".format(pwd))
if dir_existence : 
        print("directory exists")
	print("nothing to do")
else:
	print("directory doesn't exists")
	print("move the  backup data to the directory using the rsync command")
	shell_exec("sudo rsync -ai /tmp/eduonix {}/eduonix".format(pwd))



