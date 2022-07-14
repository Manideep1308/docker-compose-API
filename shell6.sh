echo "Installing docker in Vm.."

sshpass -p $2 ssh -o StrictHostKeyChecking=No $1@$3 "sh dockerinstall.sh"