echo "Copying files from container to EC2...."

scp -o StrictHostKeyChecking=No -i "~/.ssh/$1.pem" $2 $3@$4:$5