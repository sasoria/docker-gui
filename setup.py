import setuptools
import sys
import app

if sys.version_info.major < 3 or sys.version_info.minor < 5:
    print("error: docker-gui requires Python 3.5 or greater.", file=sys.stderr)
    quit(1)


try:
    LONG_DESC = open('README.md').read()
except IOError as error:
    LONG_DESC = '-'
    pass

VERSION = app.__version__
DOWNLOAD = "https://github.com/sasoria/docker-gui/archive/master.zip"


setuptools.setup(
    name="docker-gui",
    packages=setuptools.find_packages(),
    version=VERSION,
    author="Sergio Soria",
    author_email="sergio.ar.soria@gmail.com",
    description="A lightweight, easy to use docker gui in GTK3",
    long_description=LONG_DESC,
    license="GPL3",
    url="https://github.com/sasoria/docker-gui",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications :: GTK",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points={
        "console_scripts": ["docker-gui=app.__main__:main"]
    },
    python_requires=">=3.5",
    install_requires=[
        'docker>=3.7.0',
    ],
    include_package_data=True,
    data_files=[('bin/', ['app/data/start.sh'])]
)





