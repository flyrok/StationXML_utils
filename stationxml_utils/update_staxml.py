#!/usr/bin/env python

'''
Plot net/station/channel response files (bode)
and report sensitivities

'''

from obspy import read_inventory
from obspy.core import UTCDateTime
from obspy.core.inventory.response import _pitick2latex
import numpy as np
import sys,argparse
import os.path
import sys

progname='update_staxml';
__version_info__ = ('2019','12','05','0.01')
__version__ = '-'.join(__version_info__)

def print_stas(inv):
    print("Here are your N.S.C.L choices.....\n")
    try:
        conts=inv.get_contents()
        for i in conts['channels']:
            print(i)
    except Exception as e:
        print(e)

def set_coords(stainv,coords):
    _name='set_coords'
    if len(coords) == 3:
        lat=float(coords[0])
        lon=float(coords[1])
        elev=float(coords[2])
    elif len(coords) == 2:
        lat=float(coords[0])
        lon=float(coords[1])
        elev=0.0
    else:
        print(f"{_name}: Coords not set right. This is what I have: {coords}")
        return
    # need 1 network and 1 station in inventory
    if len(stainv.networks) == 1:
        if len(stainv[0].stations) == 1:
            print(stainv[0])
        else:
            print(f"{_name}: More than 1 sta in inventory")
            return
    else:
        print(f"{_name}: More than 1 net in inventory")

    for chan in stainv[0][0]:
        chan.latitude=lat
        chan.longitude=lon
        chan.elevation=elev


def main():
    parser = argparse.ArgumentParser(prog=progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=
            'Update a StationXML file with new info')

    parser.add_argument("-i","--staxml", type=str,
        required=True, help="Name of the station xml file")

    parser.add_argument("-s","--SEEDid", type=str,
        required=False, help="Seed ID to process (partial or complete Net.Station.LocationCode.Chan). Leave blank to get a list of all available in StaXML file")

    parser.add_argument("-c","--coords",nargs='+', 
        required=False, help="Change the lat,lon,elev of the selected sta.loc. Needs to specifiy lat,lon,elev(m). If elev not specified, defaults to 0.0")

    parser.add_argument("-o","--outxml",type=str, default=None,
        required=False, help="Output staxml name. If not given, defaults to input name")

    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")

    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    inv_name=args.staxml
    coords=args.coords
    debug=args.verbose
    inv=read_inventory(inv_name)

    if args.outxml:
        outxml=args.outxml
    else:
        outxml=inv_name

    if not args.SEEDid:
        print_stas(inv)
        sys.exit(0)

    seedid=args.SEEDid.split(".")

    # inv.select creates shallow copy
    if len(seedid) == 4:
        stainv=inv.select(network=seedid[0],station=seedid[1],location=seedid[2],channel=seedid[3])
    elif len(seedid) == 3:
        stainv=inv.select(network=seedid[0],station=seedid[1],location=seedid[2])
    elif len(seedid) == 2:
        stainv=inv.select(network=seedid[0],station=seedid[1])
    else:
        print('SeedID needs at least net,sta code')
        sys.exit(0)

    if coords:
        print(f"Setting new coordinates {coords}")
        set_coords(stainv,coords)

        # sync Station coords this way, because I can figure it out otherwise
        for net in inv:
            for sta in net:

                sta.latitude=sta[0].latitude
                sta.longitude=sta[0].longitude
                sta.elevation=sta[0].elevation
    else:
        print("Tell me something to do")
        parser.print_help()
    stainv[0][0].latitude=stainv[0][0][0].latitude
    inv.write(outxml,format='STATIONXML')         

if __name__ == '__main__':
    main()

