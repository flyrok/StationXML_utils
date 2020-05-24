#!/usr/bin/env python3.7

from obspy import read_inventory
import sys,argparse
from geojson import Point, Feature, FeatureCollection, dump

def parse_staxml(staxml):
    ### READ Inventory and return appropriate dict for format
    inv=read_inventory(staxml)
    stainfo=[]
    stasdict={}
    features = []
    for i in range(0,len(inv.networks)): # iter networks
        net=inv.networks[i]
        net_code=net.code
        for j in range(0,len(net)): # iter stations
            sta=net[j]
            sta_code=sta.code
            sta_ondate=sta.creation_date.strftime("%Y%j")
            if sta.end_date:
                sta_enddate=sta.end_date.strftime("%Y%j")
            else:
                sta_enddate='2599001'
            lat=sta.latitude
            lon=sta.longitude
            elevation=sta.elevation
            chans=[]
            for k in range(0,len(sta)): # iter chann
                chan=sta[k]
                code=chan.code
                loc=chan.location_code
                chans.append(f'{net_code}.{sta_code}.{loc}.{code}')
        description='\n'.join(chans)
        features.append(Feature(geometry=Point((longitude,latitude)),properties={'description':description}))
    return FeatureCollection(features)

def write_file(collection,output):
    with open(output, 'w') as f:
       dump(collection, f)
    

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=
                'Read sta info from StationXML and output to limited geojson file')
    parser.add_argument("-s","--staxml", required=True,
        help="StationXML file")
    parser.add_argument("-o","--outfile",required=True,
        help="output text file")
    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")
    args = parser.parse_args()
    staxml=args.staxml
    output=args.outfile

    collection=parse_staxml(staxml,outformat)
    write_file(collection,output)

if __name__ == '__main__':
    main()


        
