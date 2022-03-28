#!/usr/bin/env python

'''
Make a stationxml file with response info.

First cut. Rough Script. 
'''

from obspy.core import read, UTCDateTime
from obspy import read_inventory
from obspy.core.inventory import Inventory, Network, Station, Channel, Site, Equipment,Response
import sys,argparse
import os.path

# Defaults
sps=200
depth=0.0
elev=100
geolat=37.1366
geolon=-116.1493
geoelev=1528
scode="L4"
date="2018,05,30"
longname="NNSS"
netc="DT"
locs=["00", "00", "00","00","00","00"]
azims=["0.0","0.0","90.0","0.0","0.0","90.0"]
dips=["-90.0","0.0","0.0","-90.0","0.0","0.0"]


def main():
    sps=200.0
    inv = Inventory(networks=[],source="Weston")
    net = Network(code='DT',stations=[])

    zeros=[0,0,0]
    poles=[(-0.00867+0j), (-0.0168+0j), (-0.1269+0j)]
    sens=0.15/0.000000596046

    response=Response.from_paz(zeros,poles,sens,pz_transfer_function_type='LAPLACE (HERTZ)')
    sta_code='TEST'
    sta_lat=1.0
    
    sta_lon=1.0
    
    sta_elev=1.0
   
    sta_ondate='2018,01,01'
    
    sta_offdate='2599,01,01'
    
    sta_sitename='TESTER'
    
    sta = Station(
        code=sta_code,
        latitude=sta_lat,
        longitude=sta_lon,
        elevation=sta_elev,
        creation_date=UTCDateTime(sta_ondate),
        site=Site(name=sta_sitename))
        # add station to network 
    net.stations.append(sta)
    
        # Default chan info
    coords={'latitude':sta_lat,
            'longitude': sta_lon,
            'elevation': sta_elev,
            'depth': 0.0,
            'sample_rate':sps}
    chans='HDF'
    n=0
    for j in chans.split(','):
        n+=1
        chantmp=j
        chan = Channel(
                code=chantmp,
                location_code='00',
                latitude=coords['latitude'],
                longitude=coords['longitude'],
                elevation=coords['elevation'],
                depth=coords['depth'],
                azimuth=0.0,
                dip=0.0,
                sample_rate=coords['sample_rate'],
                sensor=Equipment(description='Hyperion'))
        chan.response=response
        sta.channels.append(chan)
    
    inv.networks.append(net)
    inv.write('test.xml',format="STATIONXML")

if __name__ == '__main__':
    try:
        main()
    except BufferError as e:
        print("\nExiting ...")
    except KeyboardInterrupt as e:
        print('\nExiting ...')

