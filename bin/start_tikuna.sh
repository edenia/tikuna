#!/bin/bash

docker rm -f tikuna
docker run -it --name tikuna -v /data:/home/tikuna/app/data -p 8890:8890 -p 4444:4444 tikuna:latest /bin/bash
