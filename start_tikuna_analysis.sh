#!/bin/bash

docker rm -f tikuna-analysis
docker run -d --name tikuna-analysis -v /data:/home/tikuna/app/data tikuna:latest "/home/tikuna/app/analysis/run_analysis.sh"
docker logs -f tikuna-analysis
