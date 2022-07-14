echo "docker composing up..."

ssh -o StrictHostKeyChecking=No -i "~/.ssh/$1.pem" $2@$3 "sudo docker-compose -f $4 up -d"