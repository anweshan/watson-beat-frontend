#!/bin/bash


# Defines the home of Watson Beat. Need to have a way of setting this
if [ ! -f WBHOME ]; then
    echo "Setting up Watson Beat repo"
    ./init.sh
fi

WB_HOME=$(cat WBHOME)

# Parse passed parameters
while getopts ":i:m:o:" opt; do
  case $opt in
    i)
      INIFILE=$OPTARG >&2
      ;;
    m)
      MIDIFILE=$OPTARG >&2
      ;;
    o)
      OUTPUTPATH=$OPTARG >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# Set default values if not set explicitly
if [ -z $INIFILE ]; then
    INIFILE="Ini/Space.ini"
fi

if [ -z $MIDIFILE ]; then
    MIDIFILE="Midi/mary.mid"
fi

if [ -z $OUTPUTPATH ]; then
    OUTPUTPATH="./output/"
fi

# Echo parameter values
echo "Parameters set:"
echo "INI File - $INIFILE"
echo "MIDI File - $MIDIFILE"
echo "Output path - $OUTPUTPATH"

# Remove existing output
echo "Removing existing output, if any."
rm -rf $OUTPUTPATH

cd $WB_HOME/src/;
echo "Changing directories. Currently in `pwd`"

# Generate the melody using the parameters
echo "Generating the melody..."
python wbDev.py -i $INIFILE -m $MIDIFILE -o $OUTPUTPATH
