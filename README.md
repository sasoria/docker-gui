# docker-gui
A lightweight graphical interface for docker in GTK 3. This app displays docker containers and docker images. It also allows users to run images, kill containers and displays information about containers and images. The latter as a dockerfile of the selected image.

## Install
```
$ git clone https://github.com/sasoria/docker-gui.git
$ cd docker-gui
$ pip3 install .
```

## Run
```
$ python3 app/__main__.py
```

## Requiremnts

### npm
```
$ npm install meow
$ npm install dockerode
``` 
### [dfimage](https://github.com/52cik/dockerfile-from-image)
``` 
$ git clone https://github.com/52cik/dockerfile-from-image.git
```
Make `bin/dfimage` executable with `chmod 775` and put it in your `PATH`.

## Notes
This app requires docker to be managed as a non-root user. See [Post-installation steps for Linux
](https://docs.docker.com/install/linux/linux-postinstall/) for further details.

## Example
![Container](https://github.com/sasoria/docker-gui/blob/master/docs/containers_cropped.png)

![Images](https://github.com/sasoria/docker-gui/blob/master/docs/images_cropped.png)



