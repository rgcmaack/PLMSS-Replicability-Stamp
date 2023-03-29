# Preliminaries
The package was tested on an "Ubuntu 20.04.5 LTS", but should work with any Linux distribution able to run docker.

# Installation and execution
First, install docker on your system (see https://docs.docker.com/engine/install/ for details).
Then run "build-docker.sh" ( ./build-docker.sh ).
Wait until the docker image finished building. This will require quite some time as Paraview and TTK must be built (55 minutes on an i7-9750H CPU @ 2.60GHz laptop).
The folder containing this README should now contain a "noisyTerrainMSS.jpg" reproducing Figure 6a. 
