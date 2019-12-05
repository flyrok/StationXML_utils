#!/usr/bin/env python3


from obspy import UTCDateTime
import argparse
from pathlib import Path
from sys import exit
from obspy.io.xseed import Parser
from obspy.io.xseed.core import _parse_to_inventory_object as d2inv
from obspy.core.inventory import Inventory, Network, Station, Channel, Site
import types
here = Path(__file__).resolve().parent
exec(open(here / "version.py").read())


def dataless_parser(dfiles,subset,debug=0):
    print('Using: ',subset,' please')
    inv=Inventory()
    for i in dfiles: # loop through dataless files
        p=Parser()
        if (debug):
            print('reading',i)
        try:
            p.read(i)
        except Exception as e:
            print(e)
        invtmp=d2inv(p)
        if len(invtmp._networks) > 1:
            print('More than 1 net in: ',i,len(invtmp._networks))
        else:
            nettmp=invtmp._networks[0].select(location='0K')
        if len(inv) == 0:
            inv._networks.append(nettmp)
        else:
            sta=nettmp[0].select(location='0K')
           # 
            inv._networks[0]._stations.append(sta)
    return inv

def main():
    # Command line parsing
    parser = argparse.ArgumentParser(prog=progname,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=
            '''
            Read dataless seed and write Staxml. \
            To add two Statioxml file.
            inv1=read_inventory('sta1.xml')
            inv2=read_inventory('sta2.xml' )
            for i in inv2._networks[0].stations:\
            inv._networks[0]._stations.append(i)\

            ''')

    parser.add_argument("-d","--dataless", nargs='+',
        required=True, help="Dataless seed files to read. Assumes all are in the same network")

    parser.add_argument("-o","--output", default=None,
        required=True, help="Output Staxaml name")

    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")

#    parser.add_argument('--version', action='version',
#                    version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    dataless=args.dataless
    output=args.output
    debug=args.verbose
    subset=f'location=\'0K\'' # this broken. Hardwired in dataless_parser function
    inv=dataless_parser(dataless,subset,debug=debug)
    inv.write(output,format='STATIONXML')



if __name__ == '__main__':
    main()

