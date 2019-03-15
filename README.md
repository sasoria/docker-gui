# docker-gui
A lightweight graphical interface for docker in GTK 3. This app displays docker containers and docker images. It also allows users to run images, kill containers and displays information about containers and images. The latter as a dockerfile of the selected image.
## Dependencies
* docker sdk
* dockerode
* npm (nodejs >= 7.6)
* meow
* [dfimage](https://github.com/52cik/dockerfile-from-image)
### npm
```
$ sudo apt install npm
$ sudo npm i -g dockerfile-from-image
```
## Install
```
$ git clone https://github.com/sasoria/docker-gui.git
$ cd docker-gui
$ sudo pip3 install .
```
## Run
```
$ docker-gui
```
## Notes
This app requires docker to be managed as a non-root user. See [Post-installation steps for Linux
](https://docs.docker.com/install/linux/linux-postinstall/) for further details.

## Example
![Container](https://github.com/sasoria/docker-gui/blob/master/docs/containers_cropped.png)

![Images](https://github.com/sasoria/docker-gui/blob/master/docs/images_cropped.png)



