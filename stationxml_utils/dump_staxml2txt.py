#!/usr/bin/env python

'''
Make a stationxml file with response info.

First cut. Rough Script. 
'''

from obspy import read_inventory
#from obspy.core.inventory import Inventory, Network, Station, Channel, Site
import sys,argparse
import os.path

progname='dump_staxml2txt.py';
__version_info__ = ('2019','04','02','0.01')
__version__ = '-'.join(__version_info__)

def dump_output(inv,output,debug):
    msgs=[]
    msg=f"loc,sta   ,loc, chan  , lat      ,  lon       , elev  ,  depth, sampr, cmpaz,cmpinc,sensor\n"
    msgs.append(msg)

    for i in range(0,len(inv.networks)): # iter networks
        net=inv.networks[i]
        net_code=net._code
        for j in range(0,len(net)): # iter stations
            sta=net[j]
            sta_code=sta._code
            for k in range(0,len(sta)): # iter chann
                chan=sta[k]
                code=chan._code
                loc=chan._location_code
                lat=chan._latitude
                lon=chan._longitude
                elev=chan._elevation
                dep=chan._depth
                sampr=chan._sample_rate
                az=chan._azimuth
                dip=chan._dip
                sensor=chan.sensor.description
                msg=f"{net_code:2s}, {sta_code:6s}, {loc:2s}, {code:6s}, {lat:9.6f}, {lon:10.6f}, {elev:6.1f}, {dep:6.1f}, {sampr:8.4f}, {az:5.1f}, {dip:4.1f}, {sensor}\n"
                msgs.append(msg)
    file = open(output,"w+")
    for i in msgs:
        file.write(i)
    file.close()

def main():
    parser = argparse.ArgumentParser(prog=progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=
            'dump a stationxml file to txt file')

    parser.add_argument("-i","--staxml", type=str,
        required=True, help="Name of the station xml file")

    parser.add_argument("-o","--output", type=str,
        required=True, help="output txt file")

    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")

    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()

    inv_name=args.staxml
    debug=args.verbose
    inv=read_inventory(inv_name)
    dump_output(inv,args.output,debug)



if __name__ == '__main__':
    main()

