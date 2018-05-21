#!/bin/bash

wb_home=$(cat WBHOME)
input_dir="$wb_home/src/$1*.mid"
echo $input_dir
echo $2
python3 midisox_py.py -M $input_dir $2
