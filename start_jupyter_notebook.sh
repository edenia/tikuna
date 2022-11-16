#!/bin/bash

nohup jupyter notebook --ip=0.0.0.0 --port=8890 &
sleep 5
jupyter notebook list
