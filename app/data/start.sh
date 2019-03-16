#!/usr/bin/env bash
#===  FUNCTION  ================================================================
#         NAME:  start.sh
#  DESCRIPTION:  Installs docker-gui dependencies.
#===============================================================================

OS=$(lsb_release -a | grep -o Ubuntu | head -1)
NPM_VER=$(npm -version)
NODE_VER=$(node --version | tr -d v | cut -d . -f 1,2 | tr -d ".")

echo $OS
echo $NPM_VER
echo $NODE_VER

function usage () {
    echo "this script will
    * install npm
    * install dfimage
    * install docker (optional)
    * add $USER to group <docker> (optional)"
}

function check_os () { 
	if [ -n $OS ]; then
		echo "running ubuntu..."
        return 0;
    else
        echo "exit : please run this script in ubuntu"
        exit 1;
    fi
}

function check_node () {
    if [ $NODE_VER -lt 76 ]; then
        echo "Exit : please install a node version >= 7.6 to run this script";
        return 1;
    else
        return 0
    fi
}

function install_npm () {
    if [ -n $NPM_VER ]; then
        echo "npm already installed"
    else
        echo "Installing npm"
        sudo apt install npm
        echo "npm install done."
    fi
}

function install_docker () {
    read -p "do you want to install docker.io (y/n)? " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Installing docker.io"
        sudo apt install docker.io
        echo "docker.io install done"
    fi
}

function setup_docker () {
    read -p "do you want add $USER to group <docker> (y/n)? " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "setting up docker group"
        sudo groupadd docker
        sudo usermod -aG docker $USER
        echo "$USER added to group <docker>"
    fi
}

function install_dfimage () {
    if [ $(npm list -g dockerfile-from-image | grep -o dockerfile) ]; then
        echo "dfimage already installed"
    else
        echo "Installing dfimage"
        sudo npm i -g dockerfile-from-image
        echo "dfimage install done"
    fi
}

function main () {
    usage
    check_os

    install_npm
    install_dfimage
    check_node

    install_docker
    setup_docker

    echo "install done"
}

main