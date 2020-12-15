# ScriptLauncher
A Python GUI for launching your own Python scripts.

This desktop app uses pycoffeece, a package for scripting office work automations.

To run this project you must have Python3.6 or a later version installed.


## Table of contents
* [Install](#install)
* [Launch](#launch)
* [Setup](#setup)
* [Some advice](#some-advice)

## Install
Download this repository and put it on a folder.
Then just need to install dependencies listed on "requirements.txt". You can do it using `pip`:
```
pip install -r requirements.txt
```


## Launch
To launch the application just use the command line and move to the app folder.
Then run the following command:
```
python MainApplication.py
```


## Setup
Once ScriptLauncher is open, use the menu bar to set the source directory:
- Go to 'Settings' > 'Source Directory'.
- A pop-up will ask you for a source folder. Navigate to your scripts folder and click on 'Accept'.


## Some advice
To keep things clean and mantainable don't put large projects on the scripts folder. Instead, make a `launch_LARGE_PROJECT.py` file that runs the project and put the new file on the scripts folder.
