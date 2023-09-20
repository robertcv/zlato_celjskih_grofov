# Zlato Celjskih Grofov
Android application to track investment gold profit based on Zlatarna Celje prices.

### Install dependency

```commandline
sudo apt update
sudo apt install adb
```

from https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android
```commandline
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

from https://github.com/kivy/buildozer/blob/master/Dockerfile
```commandline
sudo apt install -y \
    autoconf \
    automake \
    build-essential \
    ccache \
    cmake \
    gettext \
    git \
    libffi-dev \
    libltdl-dev \
    libssl-dev \
    libtool \
    openjdk-17-jdk \
    patch \
    pkg-config \
    python3-pip \
    python3-setuptools \
    sudo \
    unzip \
    zip \
    zlib1g-dev
```

Python dependencies

```commandline
pip3 install kivy
pip3 install buildozer
pip3 install Cython==0.29.33
```

## Build and run

Just build the apk
```commandline
buildozer android debug
```

Build, deploy to android phone and run
```commandline
buildozer android debug deploy run
```
