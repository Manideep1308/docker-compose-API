echo "Copying files to  VM.."

sshpass -p $2 scp -o StrictHostKeyChecking=No $4 $1@$3:$5