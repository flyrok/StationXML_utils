#!/usr/bin/env python

'''
Make a stationxml file with response info.

First cut. Rough Script. 
'''

from obspy.core import read, UTCDateTime
from obspy import read_inventory
from obspy.core.inventory import Inventory, Network, Station, Channel, Site, Equipment
from obspy.core.inventory import Response
from obspy.clients.nrl import NRL
import sys,argparse
import os.path

# Defaults
sps=250
depth=0.0
elev=111
geolat=42.474228
geolon=-76.44966
geoelev=337.2
scode="B02"
date="2019,06,30"
longname="YU Netwokr"
netc="YU"
locs=["00", "00", "00","10","10","10"]
azims=["0.0","0.0","90.0","0.0","0.0","90.0"]
dips=["-90.0","0.0","0.0","-90.0","0.0","0.0"]
lsb=.3052*10**-6
sens=89.4

poles = [-20.0784 + 19.1693j, -20.0785 - 19.1693j]
zeros = [0.0 + 0.0j, 0.0 + 0.0j]
scal_fac=sens/lsb
inst_info='Minimus GS-ONE LF'

response=Response.from_paz(zeros, poles, scal_fac, stage_gain_frequency=100.0, input_units='M/S', output_units='VOLTS', normalization_frequency=100.0, pz_transfer_function_type='LAPLACE (RADIANS/SECOND)', normalization_factor=1.0)

def main():
    chans="EHZ,EHN,EHE"
    # Get StationXML file
    print(f"Interactive StaXML builder")
    print(f"Work in progress...some things hardwired\n\n")
    inv_name=input(f"Enter StationXML file name: ")
    if (os.path.isfile(inv_name)):
        inv=read_inventory(inv_name)
    else:
        print(f"Making new inventory: {inv_name}\n")
        inv = Inventory(networks=[],source="Weston")
    
    # Net code
    ques=f"Enter Network Code ({str(netc)}) :"
    net_code=str(input(ques) or netc)
    net = Network(code=net_code,stations=[])
    print(f"\n")
    
    nstas=int(input("Enter number of stations to add with same sensor/digitizer (default 1):") or 1)
    for i in range(0,nstas):
        ques="Station code ("+str(scode)+") :"
        sta_code=str(input(ques) or scode)
    
        ques="Station latitude ("+str(geolat)+") :"
        sta_lat=float(input(ques) or geolat)
    
        ques="Station longitude ("+str(geolon)+") :"
        sta_lon=float(input(ques) or geolat)
    
        ques="Station elev("+str(geoelev)+") :"
        sta_elev=float(input(ques) or geoelev)
    
        ques="Station ondate ("+str(date)+") :"
        sta_ondate=str(input(ques) or date)
    
        ques="Station offdate ("+str(date)+") :"
        sta_offdate=str(input(ques) or date)
    
        ques="Station long name ("+str(longname)+") :"
        sta_sitename=str(input(ques) or longname)
    
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
            'sample_rate': sps}
    
        n=-1
        ques=f"Enter channel names, comma separated ({chans}) :"
        chans=str(input(ques) or chans)
        for j in chans.split(','):
            n+=1
            chantmp=j
            print("Doing channel ",chantmp)
            aztmp=azims[n]
            diptmp=dips[n]
            loc=locs[n]
            for k in coords.keys():
                ques=str(chantmp)+" enter "+k+"("+str(coords[k])+"):"
                coords[k]=float(input(ques) or coords[k])
    
         
            chan = Channel(
                code=chantmp,
                location_code=loc,
                latitude=coords['latitude'],
                longitude=coords['longitude'],
                elevation=coords['elevation'],
                depth=coords['depth'],
                azimuth=aztmp,
                dip=diptmp,
                sample_rate=coords['sample_rate'],
                sensor=Equipment(description=inst_info))
            chan.response=response
            sta.channels.append(chan)
    
    inv.networks.append(net)
    inv.write(inv_name,format="STATIONXML")

if __name__ == '__main__':
    try:
        main()
    except BufferError as e:
        print("\nExiting ...")
    except KeyboardInterrupt as e:
        print('\nExiting ...')

