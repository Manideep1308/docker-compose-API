echo "Installing Docker in Ec2..."

ssh -o StrictHostKeyChecking=No -i "~/.ssh/$1.pem" $2@$3 "sh dockerinstall.sh"