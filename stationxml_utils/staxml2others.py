#!/usr/bin/env python3.7

from obspy import read_inventory
from obspy.core import UTCDateTime
import sys,argparse

def dec2ddmm(lon,lat):
    is_positive_lat = lat >= 0
    is_positive_lon = lon >= 0
    lon= abs(lon)
    lat= abs(lat)
    lon_deg,lon_min = divmod(lon*60,60)
    lat_deg,lat_min = divmod(lat*60,60)
    latv = 'N' if is_positive_lat else 'S'
    lonv = 'E' if is_positive_lon else 'W'
    return(int(lon_deg),lon_min,lonv,int(lat_deg),lat_min,latv)

def parse_staxml(staxml,outformat):
    ### READ Inventory and return appropriate dict for format
    inv=read_inventory(staxml)
    stainfo=[]
    stasdict={}
    for i in range(0,len(inv.networks)): # iter networks
        net=inv.networks[i]
        net_code=net._code
        for j in range(0,len(net)): # iter stations
            sta=net[j]
            sta_code=sta._code
            sta_ondate=sta._creation_date.strftime("%Y%j")
            for k in range(0,len(sta)): # iter chann
                chan=sta[k]
                code=chan._code
                loc=chan._location_code
                lat=chan._latitude
                lon=chan._longitude
                elev=chan._elevation
                start_date=chan.start_date
                end_date=chan.end_date
                hang=chan._azimuth
                vang=chan._dip
                if outformat == 'binder':
                    lond,lonm,lonv,latd,latm,latv=dec2ddmm(lon,lat) 
                    stainfo.append({'net':net_code,'sta':sta_code,
                        'chan':code,'loc':loc,'latd':latd,'latm':latm,'latv':latv,
                        'lond':lond,'lonm':lonm,'lonv':lonv,'elev':elev})
                elif outformat == 'csv':
                    stainfo.append({'net':net_code,'sta':sta_code,
                        'chan':code,'loc':loc,'lat':lat,'lon':lon,'elev':elev})
                elif outformat == 'css': 
                    if start_date:
                        ondate=int(start_date.strftime('%Y%j'))
                    elif sta_ondate:
                        ondate=int(sta_ondate)
                    else:
                        ondate=1970001
                    if end_date:
                        offdate=int(end_date.strftime("%Y%j"))
                    else:
                        offdate=2599001

                    stainfo.append({'net':net_code,'sta':sta_code,
                        'chan':code,'loc':loc,'lat':lat,'lon':lon,'elev':elev,
                        'ondate':ondate,'offdate':offdate,'hang':hang,'vang':vang})
                else:
                    stainfo.append({'net':net_code,'sta':sta_code,
                        'chan':code,'loc':loc,'lat':lat,'lon':lon,
                        'elev':elev})
    
                #dep=chan._depth
                #sampr=chan._sample_rate
                #az=chan._azimuth
                #dip=chan._dip
                #sensor=chan.sensor.description
    return stainfo

def write_file(stainfo,output,outformat):
    msgs=[]
    msgs2=[]
    if outformat == 'cvs':
        for i in stainfo:
            sta=i['sta']
            net=i['net']
            chan=i['chan']
            lat=i['lat']
            lon=i['lon']
            elev=i['elev']
            msgs.append(f"{sta:<5s},{net:<2s},{chan:<4s},{lat:9.5f},{lon:10.5f}{elev:6.1f}\n")

    if outformat == 'nll':
        stalist=[]
        for i in stainfo:
            sta=i['sta']
            chan=i['chan']
            lat=i['lat']
            lon=i['lon']
            elev=i['elev']/1000
            if sta not in stalist:
#                GTSRCE    MMS     LATLON    37.6304      -119.0317    0     3.324
                msgs.append(f"GTSRCE {sta:>6s}    LATLON  {lat:10.4f} {lon:14.4f}   0  {elev:9.3f}\n")
                stalist.append(sta)
    
    if outformat == 'css':
        stalist=[]
        for i in stainfo:
            sta=i['sta']
            chan=i['chan']
            lat=i['lat']
            lon=i['lon']
            elev=i['elev']
            ondate=i['ondate']
            offdate=i['offdate']
            hang=i['hang']
            vang=i['vang']
            staname='none'
            refsta=staname=ctype=descrip=statype='-' 
            deast=dnorth=0.0000
            edepth=-9.9999
            chanid=-1
            lddate=UTCDateTime.utcnow().timestamp
            if sta not in stalist:
                msgs.append(f"{sta:>6s} {ondate:8d} {offdate:8d} {lat:9.4f} {lon:9.4f} {elev:9.4f} {staname:>50s} {statype:>4s} {refsta:>6s} {dnorth:9.4f} {deast:9.4f} {lddate:17.5f}\n")
                stalist.append(sta)
            msgs2.append(f"{sta:>6s} {chan:>8s} {ondate:8d} {chanid:8d} {offdate:8d} {ctype:>4s} {edepth:9.4f} {hang:6.1f} {vang:6.1f} {descrip:>50s} {lddate:17.5f}\n")
    
    if outformat == 'binder':
        # this format is like hypoinverse
        #S08   YU  EHN  35 44.5793N 97 16.1719W  323.0   A 0.00  0.00  0.00  0.00 1  0.00-- 1.000
        msgs=[]
        for i in stainfo:
            sta=i['sta']
            net=i['net']
            chan=i['chan']
            latd=i['latd']
            latm=i['latm']
            latv=i['latv']
            lond=i['lond']
            lonm=i['lonm']
            lonv=i['lonv']
            elev=i['elev']
            other=f"A 0.00  0.00  0.00  0.00 1  0.00{i['loc']} 1.000"
            msgs.append(f"{sta:<5s} {net:<2s}  {chan:<4s} {latd:2d} {latm:7.4f}{latv} {lond:2d} {lonm:7.4f}{lonv} {elev:6.1f}   {other}\n")

    if outformat == 'cnv':
        # velest format
        msgs=[]
        msgs.append("#(a4,f7.4,a1,1x,f8.4,a1,1x,i4,1x,i1,1x,i3,1x,f5.2,2x,f5.2)\n")
        msgs.append("#\n")
        for n,i in enumerate(stainfo):
            chan=i['chan']
            if 'Z' not in chan: 
                continue
            sta=i['sta']
            lat=i['lat']
            lon=i['lon']
            if lat > 0:
                latv='N'
            else:
                latv='S'
            if lon > 0:
                lonv='E'
            else:
                lonv='W'
            elev=i['elev']
            msgs.append(f"{sta:4s}{abs(lat):7.4f}{latv} {abs(lon):8.4f}{lonv} {int(elev):04d} 1 {n:03d} 00.00  00.00   1\n")

    if outformat == 'pick_ew':
        msgs=[]
        msgs.append("#  This is a sample station list for the pick_ew program.")
        msgs.append("#\n")
        msgs.append("#                                 MinBigZC       RawDataFilt    LtaFilt         DeadSta          PreEvent\n")
        msgs.append("# Pick  Pin    Station/      MinSmallZC   MaxMint           StaFilt       RmavFilt           AltCoda\n")
        msgs.append("# Flag  Numb   Comp/Net/Loc   Itr1   MinPeakSize  i9  CharFuncFilt  EventThresh          CodaTerm         Erefs   ClipCount\n")
        msgs.append("# ----  ----   --------   ---------------------------------------------------------------------------------------------\n")
        pick_flag=1
        pin=0
        for i in stainfo:
            sta=i['sta']
            chan=i['chan']
            net=i['net']
            loc=i['loc']
            itr1=3
            minSmallZC=40
            minBigZC=3
            minPeakSize=60
            MaxMint=500
            i9=1
            RawDataFilt=1.0
            CharFuncFilt=3
            StaFilt=0.6
            LtaFilt=0.03
            EventThresh=5.0
            RmavFilt=0.99
            DeadSta=120000
            CodaTerm=49.14
            AltCoda=0.8
            PreEvent=1.5
            Erefs=50000.
            ClipCount=4096
            msgs.append(f"{pick_flag} {pin} {sta} {chan} {net} {loc} {itr1} {minSmallZC} {minBigZC} {minPeakSize} {MaxMint} {i9} {RawDataFilt} {CharFuncFilt} {StaFilt} {LtaFilt} {EventThresh} {RmavFilt} {DeadSta} {CodaTerm} {AltCoda} {PreEvent} {Erefs} {ClipCount}\n")
                        #1     0  AAR   VHZ NC  -- 3  40  3  60  500  3  .985  3.  .6  .03  5.  .9961  1200.  49.14  .8  1.5  50000.     2048
            pin+=1
    
    if outformat == 'pick_fp':
        msgs=[]
        msgs.append("# Do not leave any blank lines in this file.\n")
        msgs.append("#\n")
        msgs.append("#\n")
        msgs.append("# Note: use negative values for filterWindow, longTermWindow\n")
        msgs.append("#       and tUpEvent to let the code autoset them.\n")
        msgs.append("#\n")
        msgs.append("#                                      threshold1\n")
        msgs.append("# Pick  Pin     Sta/Comp           longTermWindow  tUpEvent\n")
        msgs.append("# Flag  Numb    Net/Loc       filterWindow  threshold2\n")
        msgs.append("# ----  ----    --------      -----------------------------\n")
        pin=0
        for i in stainfo:
            chan=i['chan']
            if 'Z' not in chan: 
                continue
    #        if chan[2] != 'Z': # only do Z chans
    #            continue
            flag=1
            pin+=1
            sta=i['sta']
            net=i['net']
            loc=i['loc']
            filtwin=1. # defaults to 300*1/samprate
            longwin=4.
            thresh1=8.6       
            thresh2=10.2
            tUp=0.016
            msgs.append(f"   {flag}     {pin:02d}   {sta:>5s} {chan:>3s} {net:>2s} {str(loc)} {filtwin:0.1f} {longwin:0.1f} {thresh1:0.3f} {thresh2:0.3f} {tUp:f}\n")
    #        msg=f"{i['sta']:>6s} {i['net']:>2s} {i['chan']:>4s} {i['latd']:2d} {i['latm']:7.4f} {i['lond']:2d} {i['lonm']:7.4f} {i['elev']:6.1f} A 0.00  0.00  0.00  0.00 1  0.00-- 1.000"
  
  
    # loop through messages and write output 
    if outformat == 'css':  # if css, then make .site file
        output=output + '.site' 

    file = open(output,"w+")
    for i in msgs:
        file.write(i)
    file.close()

    if len(msgs2) > 0:  # this is only for css output
        output=output + 'chan' # this make .sitechan table
        file = open(output,"w+")
        for i in msgs2:
            file.write(i)
        file.close()
    

def main():
    outformats=['binder', 'pick_fp', 'csv','css','nll','pick_ew','cnv']
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=
                'Read sta info from StationXML and output to various txt file')
    parser.add_argument("-s","--staxml", required=True,
        help="StationXML file")
    parser.add_argument("-o","--outfile",required=True,
        help="output text file")
    parser.add_argument("-f","--format",required=True,
        help=f"output format: {outformats}")
    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")
    args = parser.parse_args()
    staxml=args.staxml
    output=args.outfile
    outformat=args.format

    format_good=0
    for i in outformats:
        if outformat == i:
            format_good=1
    if format_good == 0:
        print("Output format ",outformat," not recognized. Try again")
        sys.exit(0)

    stainfo=parse_staxml(staxml,outformat)
    write_file(stainfo,output,outformat)

if __name__ == '__main__':
    main()


        
