echo "docker composing down..."

ssh -o StrictHostKeyChecking=No -i "~/.ssh/$1.pem" $2@$3 "sudo docker-compose -f $4 down"