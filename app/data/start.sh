#!/usr/bin/env bash
#===  FUNCTION  ================================================================
#         NAME:  start.sh
#  DESCRIPTION:  Installs docker-gui dependencies.
#===============================================================================

function usage () {
    echo "Usage :  $0 [options] [--]

    Options:
    -h   Display this message
    -n   Install with node dependencies
    "
}

function check_os () {
    if [[  ]]; then
        echo "Please run this in an apt based os";
        exit 1;
    fi
}

function check_npm () {
    if [[  ]]; then
        echo "npm already installed";
    exit 1;
    fi
}

function install_npm () {
    echo "Installing npm";
    sudo apt install npm
    echo "npm install done.";
}

function install_meow () {
    echo "Installing meow";
    npm install meow
    echo "npm install done.";
}

function install_dockerode () {
    echo "Installing npm";
    npm install dockerode
    echo "npm install done.";

}

function clean_up () {
  # potential rm -rf
}

function main () {
  getargs "$@";

  clean_up;
}

main "$@"