#!/usr/bin/env python

'''
Plot stations on map 

'''

from obspy import read_inventory

# matplot lib stuff
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
    AutoMinorLocator)
# special matplot lib
from mpl_toolkits.basemap import Basemap

import numpy as np
import sys,argparse
import sys

progname='plot_staxml';
__version_info__ = ('2020','05','03','0.01')
__version__ = '-'.join(__version_info__)

def tick_stride(mrange,decimals):
    fmajor=np.round(mrange/4,decimals=decimals)
    fminor=fmajor/4
    return fmajor,fminor

def get_stacoords(inv_infile):
    sta_coords={}
    try:
        inv=read_inventory(inv_infile)
    except Exception as e:
        print(f'Problem reading {inv} ...\n\t{e}')
        return sta_coords

    # get all sta coords from StationXML
    for i in range(0,len(inv.networks)): # iter networks
        net=inv.networks[i]
        net_code=net._code
        for j in range(0,len(net)): # iter stations
            sta=net[j]
            sta_code=sta._code
            lat=sta.latitude
            lon=sta.longitude
            sta_coords[sta_code]=[lon,lat] # third fields is 1 if used in location
    return sta_coords

def get_bounds(sta_coords,decimals,extent):

    if isinstance(extent,(list)):
        return extent
    
    vals=list(sta_coords.values())
    lons=sorted([v[0] for v in vals])
    lats=sorted([v[1] for v in vals])
    # make map square
    lon_rng=abs(lons[-1] - lons[0])
    lat_rng=abs(lats[-1] - lats[0])
    lon_diff=0
    lat_diff=0
    if lon_rng > lat_rng:
        lat_diff=(lon_rng-lat_rng)/2
    else:
        lon_diff=(lat_rng - lon_rng)/2
    lonmin=np.round(min(lons) + -1*lon_diff,decimals)
    lonmax=np.round(max(lons) + lon_diff,decimals)
    latmin=np.round(min(lats) + -1*lat_diff,decimals)
    latmax=np.round(max(lats) + 1*lat_diff,decimals)

    extent=[lonmin,latmin,lonmax,latmax]
    print(extent)
    return(extent)

def plot_map(inv_file,decimals,extent,excludes,outpng):

    sta_coords=get_stacoords(inv_file) # get station coordinates
    extent=get_bounds(sta_coords,decimals,extent)
    print(extent)
#    sys.exit(0)
    fig = plt.figure(dpi=200,figsize=(6,6.5))
    ax=fig.add_subplot(111)
    map=Basemap(llcrnrlon=extent[0],llcrnrlat=extent[1],urcrnrlon=extent[2],urcrnrlat=extent[3],epsg=3857,suppress_ticks=True)
    xpix=2000
    v=False
    map.arcgisimage(service='Specialty/DeLorme_World_Base_Map',xpixels=xpix, verbose=v,aspect='auto',extent=extent)

    c_all=(83/255,39/255,234/255,1)
    for k in sta_coords.keys():
        if not k in excludes:
            lon=sta_coords[k][0]
            lat=sta_coords[k][1]
            x, y = map(lon, lat)
            map.scatter(x,y,marker="^",color=c_all,s=30,linewidths=0.5,edgecolor='black')
            ax.annotate(str(k),xy=(x,y), fontsize=6, xytext=(2,2),textcoords='offset points')

# Add lat lon lables to map
    newax = fig.add_axes(ax.get_position(), frameon=True)
    newax.set_xlim(map.lonmin,map.lonmax)
    newax.set_ylim(map.latmin,map.latmax)
    newax.set_frame_on(True)
    newax.patch.set_visible(False)

    xmajor,xminor=tick_stride(map.lonmax-map.lonmin,2)
    ymajor,yminor=tick_stride(map.latmax-map.latmin,2)
    newax.xaxis.set_major_locator(MultipleLocator(xmajor))
    newax.xaxis.set_major_formatter(FormatStrFormatter('%0.2f°'))
    newax.xaxis.set_minor_locator(MultipleLocator(xminor))
#
    newax.yaxis.set_major_locator(MultipleLocator(ymajor))
    newax.yaxis.set_major_formatter(FormatStrFormatter('%0.2f°'))
    newax.yaxis.set_minor_locator(MultipleLocator(yminor))
#        title=f"Events:"


    plt.savefig(outpng,format='png',bbox_inches='tight')
        


def main():
    parser = argparse.ArgumentParser(prog=progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=
            'Report Sensitivities from a StaXML file with response info. And plot response.')

    parser.add_argument("-i","--staxml", type=str,
        required=True, help="Name of the station xml file")

    parser.add_argument("-d","--decimals", type=int,default=2,
        required=False, help="Decimal precision on lat/lon")

    parser.add_argument("-b","--bounds", type=float, nargs=4, default=None,
        required=False, help="Hard set lat/lon range, as lonmin latmin lonmax latmax")

    parser.add_argument("-e","--exclude", type=str, nargs='*', default=[None],
        required=False, help="Stas to exclude from plots")

    parser.add_argument("-o","--outpng", type=str,default='junk_map.png',
        required=False, help="Name of output png file")

    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")

    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    inv_name=args.staxml
    decimals=args.decimals
    bounds=args.bounds
    excludes=args.exclude
    outpng=args.outpng
    
    plot_map(inv_name,decimals,bounds,excludes,outpng)


if __name__ == '__main__':
    main()

