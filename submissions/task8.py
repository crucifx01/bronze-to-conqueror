import os
a = input('Enter the no. of task you want to execute\n')

if(a == 1):
	myCmd = 'echo "Enter Username"; read user; echo "Enter listening_port"; read Lp; echo "Enter Port"; read port; echo "Enter Ip"; read ip; echo "Processing ..."; ssh -R $Lp:127.0.0.1:$port $user@$ip'

if(a == 2):
	myCmd = 'echo "Enter Username"; read user; echo "Enter Ip_address"; read ip; echo "Enter Port Number"; read port; echo "Enter Remote Command to be executed"; read RC; ssh $user@$ip -p $port $RC'

if(a == 3):
	myCmd = 'echo "Enter Folder to sent"; read folder_; echo "Enter Username"; read user; echo "Enter ip_address"; read ip_address; scp -r $folder_  $user@$ip_address:home/remote/week-1 '

if(a == 4):
	myCmd = 'echo "Enter Username"; read user; echo "Enter ip_address"; read ip; sftp user@ip '

if(a == 5):
	myCmd = ' echo "Enter Username"; read username; echo "Enter Password"; read password; echo "Enter Host"; read host; echo "Enter Port"; read port; export http_proxy="http://$username:$password@$host:$port"; export https_proxy="https://$username:$password@$host:$port"; export ftp_proxy="ftp://$username:$password@$host:port" '

os.system(myCmd)

print 'Done'