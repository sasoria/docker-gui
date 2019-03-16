#!/usr/bin/env bash
#===  FUNCTION  ================================================================
#         NAME:  start.sh
#  DESCRIPTION:  Installs docker-gui dependencies.
#===============================================================================

function usage () {
    echo "this script will
    * install npm
    * install dfimage
    * install docker (optional)
    * add $USER to group <docker> (optional)"
}

function check_os () {
    OS=$(lsb_release -a | grep -o Ubuntu | head -1)

	if [ -n $OS ]; then
		echo "[start.sh] running ubuntu..."
        return 0;
    else
        echo "[start.sh] exit : please run this script in ubuntu"
        exit 1;
    fi
}

function check_node () {
    if [ -P node ]; then
        NODE_VER=$(node --version | tr -d v | cut -d . -f 1,2 | tr -d ".")
    else
        NODE_VER=0
    fi

    if [ $NODE_VER -lt 76 ]; then
        echo "[start.sh] exit : please install a node version >= 7.6 to run this script";
        return 1;
    else
        return 0
    fi
}

function install_npm () {
    if [ -P npm ]; then
        echo "[start.sh] npm already installed"
    else
        echo "[start.sh] installing npm..."
        sleep 1000
        sudo apt install npm
        echo "[start.sh] npm install done."
    fi
}

function install_docker () {
    read -p "[start.sh] do you want to install docker.io (y/n)? " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "[start.sh] installing docker.io ..."
        sleep 1000
        sudo apt install docker.io
        echo "[start.sh] docker.io install done"
    fi
}

function setup_docker () {
    read -p "[start.sh] do you want add $USER to group <docker> (y/n)? " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "[start.sh] setting up docker group..."
        sleep 1000
        sudo groupadd docker
        sudo usermod -aG docker $USER
        echo "[start.sh] $USER added to group <docker>"
    fi
}

function install_dfimage () {
    if [ $(npm list -g dockerfile-from-image | grep -o dockerfile) ]; then
        echo "[start.sh] dfimage already installed"
    else
        echo "[start.sh] installing dfimage..."
        sleep 1000
        sudo npm i -g dockerfile-from-image
        echo "[start.sh] dfimage install done"
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

    echo "[start.sh] install done"
    sleep 1000
}

main