# docker-gui
A lightweight graphical interface for docker in GTK 3. This app displays docker containers and docker images.

## Run
```
$ python app/__main__.py
```

## Requiremnts
### pip
```
$ pip install docker
```
### npm
```
$ npm install meow
$ npm install dockerode
``` 
### [dfimage](https://github.com/52cik/dockerfile-from-image)
``` 
$ git clone https://github.com/52cik/dockerfile-from-image.git
``` 

## Notes
This app requires docker to be managed as a non-root user. See [Post-installation steps for Linux
](https://docs.docker.com/install/linux/linux-postinstall/) for further details.

## Example
![Container](https://github.com/sasoria/docker-gui/blob/master/docs/containers_cropped.png)

![Images](https://github.com/sasoria/docker-gui/blob/master/docs/images_cropped.png)



