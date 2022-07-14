#all happens inside ec2 server

sudo apt-get -y update

sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common



curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -


sudo apt-get install -y docker-ce docker-ce-cli containerd.io

apt-cache madison docker-ce

sudo apt-get install -y docker-ce docker-ce-cli containerd.io

sudo apt install -y pass
#install docker
sudo apt install -y docker.io


#install docker compose
sudo apt install -y docker-compose


#exucute docker commands without sudo
# sudo usermod -aG docker ubuntu


#check version
sudo docker --version

#check compose version
sudo docker-compose --version
