# Preliminaries
The package was tested on an "Ubuntu 20.04.5 LTS", but should work with any Linux distribution able to run docker.

# Installation and execution
First, install docker on your system (see https://docs.docker.com/engine/install/ for details).
Then run "build-docker.sh" ( ./build-docker.sh ).
Wait until the docker image finished building. This will require quite some time as Paraview and TTK must be built (55 minutes on an i7-9750H CPU @ 2.60GHz laptop).
The folder containing this README should now contain a "noisyTerrainMSS.jpg" reproducing Figure 6a. 

# Potential errors and warnings
- If errors, regarding SSE 4.2 support on Embree and RT filters on OIDN, occour please switch to the NoSSE42 branch. There, some features have been turned of to allow compilation, but leading to a resulting image that is not denoised.
- Compiling TTK exceeds the log size limit of 2MiB. You will not be able to see the full log of that build step.
