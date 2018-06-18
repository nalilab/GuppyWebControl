# Guppy Web control

A flask server that should simplify the monitoring of camera outputs. The website assumes that new images are saved to a specific folder. For the moment we have to following abilities:

- Add a camera.
- It prints the data for the moment.
- The setting can be changed in the config page.


On the technical side we use the following ingredients:
- Updates on the client are done through flask_socketio.
- The layout is made nice through flask_bootstrap.
- Graphics are done with plotly.js

Further, we will most likely not install saving of the data on the server as this would make the whole thing MUCH more complicated (where and who to store the data. Which data should we show etc.)

# Installation

- create a new directory
- clone the repository through 'git clone ...' in the new folder
- create a new virtualenv through 'conda create -n YOURNAME python=3.6'
- activate the virtualenv through 'source activate YOURNAME'
- install the dependencies through 'pip install -r requirements.txt'
- start it through 'start.sh'
- open it in a brower on 'localhost:5000'

# Usage
## The server itself
 - activate the virtualenv through 'source activate YOURNAME'
 - start it through 'start.sh'
 - runs on 'localhost:5000' or whatever your PC is called.

## Test without Camera

 If you want to test the camera without having an camera, you can simply use the create
 test pattern function.

## Saving to hdf5

UNTESTED.

# TODO

 [ ] allow for saving to an hdf5.

 [ ] save values to a table ?

 [ ] have several cameras ?
