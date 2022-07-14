echo "docker composing up.."

sshpass -p $2 ssh -o StrictHostKeyChecking=No $1@$3 "sudo docker-compose -f $4 up -d"