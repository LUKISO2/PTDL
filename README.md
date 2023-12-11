# Prehraj.to Downloader (PTDL)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/LUKISO2/PTDL)

Downloader that downloads from prehraj.to or prehrajto.cz

## WARNING: Antivirus false positive

The antivirus may detect the launcher as a virus, this is because the launcher is not signed and created with pyinstaller. If you want to use the launcher, you can add an exception to your antivirus.

## Builds

You can download the latest windows build from the [releases](https://github.com/LUKISO2/PTDL/releases)

Linux/mac release is **not** coming soon.

If you own a mac or a linux pc, you can build the launcher yourself and it *should* work.

## How to build on windows

1. Download python 3.7+ from [the official python site](https://www.python.org/downloads/release/python-3107/) and install it (may work with older versions, but not tested)
2. Download the PTDL source code
3. Uzip the source code to a folder
4. Run `compile.bat PATH_TO_PTDL_FOLDER/PTDL-main`
5. The launcher executable should be in the "PATH_TO_PTDL_FOLDER/PTDL-main/dist" folder if everything worked correctly

## How to build on linux

> Note: This works everywhere a litlle bit different, so you may need to do some research on how to install python and pip (including tkinter and other common libraries) on your system.

1. Download python 3.7+ source code from [the official python site](https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz) (may work with older versions, but not tested)
2. Check that you have all the required libraries installed (tkinter, pip, build-essential, etc.) -> the apt-get list I used, but some parts surely can be ommited: `sudo apt-get install -y build-essential libncurses5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev libffi-dev libexpat1-dev libbz2-dev liblzma-dev tcl-dev libreadline-dev tk linux-headers-generic openssl wget`
3. Follow instructions on the internet on how to build python on your distro (reccomended to also use the `--enable-optimizations` flag, but it may not work with `--enable-shared`)
    - On most systems you can just run `./configure --prefix=/usr/local --enable-shared --with-ensurepip=install LDFLAGS="-Wl,-rpath /usr/local/lib"`, then `make`, then `make test` and finally `sudo make install` (or `sudo make altinstall` if you have multiple python versions installed)
4. Now follow the [windows instructions](#how-to-build-on-windows) skipping the part where python is downloaded and installed and repacing `build.bat` with `build.sh`

*Are you a linux user and you know how to automate this process? Feel free to make a pull request with a better build script.*

## How to use

1) Input the link to the video you want to download into the text box
2) Click the "Search" button
3) Wait for the resolution list to load
4) Select the resolution you want to download
5) Click the "Download" button
6) *A browser window should open*
7) Click on the three dots in the bottom right corner of the video and select "Download"
8) Wait for the download to finish
9) Enjoy your video
