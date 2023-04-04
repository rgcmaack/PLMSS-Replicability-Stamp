#!/bin/bash 
docker buildx build \
    --no-cache \
    --target ttk \
    -f Dockerfile \
    --load \
    -t ttk-plmss \
    .

sleep 5

temp_container=$(docker create ttk-plmss)
docker cp $temp_container:/home/noisyTerrainMSS.jpg .
docker rm -v $temp_container
