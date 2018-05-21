#!/bin/bash

# TO-DO: Improve this to not assume current directory
cd ..

# Clone the repo locally
git clone https://github.com/cognitive-catalyst/watson-beat.git

if [ -d watson-beat ]; then
    # Set WBHOME to signal that watson-beat set up has been done
    echo "../watson-beat" > bash/WBHOME
    cd watson-beat
    # Install requirements
    pip2 install -r requirements.txt --no-cache-dir
fi
