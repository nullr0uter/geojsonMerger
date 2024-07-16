# geojsonMerger
This is a small project of mine to merge geojson files in python.

# Usage
The usage of this script is simple. You have to supply two parameters like this:
```
merge_geojson.exe -i "YOUR\PATH\file1.geojson" "YOUR\PATH\file2.geojson" -o "YOUR\PATH\outputfile.geojson"
```
I´d recommend a batch script like this:
```
@echo off
merge_geojson.exe -i "YOUR\PATH\file1.geojson" "YOUR\PATH\file2.geojson" -o "YOUR\PATH\outputfile.geojson"
pause
```
You can supply as many input files as you want but only one output file.

# Used python packages
The following python packages are used (if running the python file, these have to be installed using pip for example):
```
sys
geojson
argparse
```
