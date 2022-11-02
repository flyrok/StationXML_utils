#!/usr/bin/env python3

'''
Try to merge a bunch of stationXML together
'''

from obspy import read_inventory
from obspy.core.inventory import Inventory, Network, Station, Channel, Site, Equipment

from obspy.core import UTCDateTime
import sys,argparse

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=
                'Read sta info from StationXML and output to various txt file')
    parser.add_argument("-s","--staxmls", nargs='*',required=True,
        help="StationXML files")
    parser.add_argument("-o","--outfile",required=True,
        help="Output merged staxml ")
    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")
    args = parser.parse_args()
    staxmls=args.staxmls
    output=args.outfile

    dirty_merge=Inventory()
    for staxml in staxmls: 
        dirty_merge+=read_inventory(staxml)

    net_list=[net.code for net in dirty_merge.networks]
    net_list=sorted(set(net_list))

    clean_merge=Inventory()
    for net_code in net_list: # loop through all network codes

        # select all net_code entries from dirt_merge
        tmp_inv=dirty_merge.select(network=net_code)

        tmp_net=Network(net_code)

        for net in tmp_inv.networks:

            # step 1
            # check if we've added this network to output yet
            try:
                clean_merge.select(network=net_code)
                print(f'output_staxml already has {net_code}')
            except:
                tmp_net.start_date=net.start_date
                tmp_net.end_date=net.end_date
                tmp_net.code=net.code
                tmp_net.description=net.description
                clean_merge+=tmp_net
            # Step 2
            for sta in net.stations:
                tmp_net.stations.append(sta)
        clean_merge+=tmp_net



    clean_merge.write(output,'STATIONXML')
        

if __name__ == '__main__':
    main()


        
