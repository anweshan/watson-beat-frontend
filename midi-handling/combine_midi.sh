#!/bin/bash

echo $1
echo $2
./midisox_py.py -M $1*.mid $2
