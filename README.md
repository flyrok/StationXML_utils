## StationXML_utils##

Plot the instrument response from a StationXML file, and report the sensitivities

## Install ##

Clone source package  
`git clone http://github.com/flyrok/StationXML_utils`  

Install with pip after download  
`pip install .`  

Or install directly from github  
`pip install git+https://github.com/flyrok/StationXML_utils#egg=StationXML_utils`  

Or just put the executable on your PATH and call directly  
`./staxml_respinfo.py`

## Python Dependencies ##

python>=3.6  (script uses f-strings)  
obspy (https://github.com/obspy/obspy/wiki)
-- without this, nothing will work

## Usage ##

To see help:  
`staxml_respinfo --help`    

To see version:  
`staxml_respinfo --version`    

To see a list of SEED ids in a StationXML file:  
`staxml_respinfo -i INPUT.staxml`  

To plot the response for SEED_id N4.K57A.00.HHZ:  
`staxml_respinfo -i INPUT.staxml -s N4.K57A.00.HHZ


