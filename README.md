# docker-gui
A lightweight graphical interface for docker in GTK 3. This app displays docker containers and docker images. It also allows users to run images, kill containers and displays information about containers and images. The latter as a dockerfile of the selected image. Unlike other Docker GUI's, this implementation shows the Dockerfile of running containers.

## Dependencies
* docker sdk
* dockerode
* npm (nodejs >= 7.6)
* meow
* [dockerfile-from-image](https://github.com/52cik/dockerfile-from-image)

## Install
```
$ git clone https://github.com/sasoria/docker-gui.git
$ cd docker-gui
$ sudo pip3 install .
```
## Setup
#### Ubuntu (18.04)
```
$ sudo start.sh
```
#### Other
```
$ sudo [package manager] install docker.io
$ sudo groupadd docker
$ sudo usermode -aG docker $USER

$ sudo [package manager] install npm
$ sudo npm i -g dockerfile-from-image
```

## Run
```
$ docker-gui
```
## Notes
This app requires docker to be managed as a non-root user with,
```
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
```
See [Post-installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/) for further details.
## Example
![Container](https://github.com/sasoria/docker-gui/blob/master/docs/containers_cropped.png)

![Images](https://github.com/sasoria/docker-gui/blob/master/docs/images_cropped.png)



