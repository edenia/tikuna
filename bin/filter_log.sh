#!/bin/bash

cat normal-log.log | grep removed | tr -s " " | tr = ' ' | cut -d ' ' -f 1,8,10,12,14,16  > normal-log-filtered.log
cut -d '[' -f 4 normal.log > normal-aux.log
sed -i 's/^/[2023-/' normal.log
