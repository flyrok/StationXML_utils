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

progname='staxml_respplot.py';
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

def tick_stride(mrange):
    fmajor=np.round(mrange/5,decimals=2)
    fminor=fmajor/4
    return fmajor,fminor

def get_response(stainv):
    seedid=stainv.get_contents()['channels'][0]
    sps=stainv[0][0][0].sample_rate
    df=1/sps
    start=1/600 # min freq
    stop=sps/2 # max freq
    nfreqs=int(sps/(start))+1

    freqs=np.linspace(start,stop,nfreqs)
    start_date=stainv[0][0][0].start_date
    end_date=stainv[0][0][0].end_date
    if not end_date:
        datet=start_date
    else:
        datet=end_date
    r=stainv.get_response(seedid,datet)
    resp=r.get_evalresp_response_for_frequencies(freqs,output='VEL')
    sens=r.instrument_sensitivity
    print(f"Instrument Response Sensitivity,{r}")
    value=sens.value
    in_units=sens.input_units.lower()
    out_units=sens.output_units.lower()
    freq=sens.frequency
   
    return freqs,resp,value,in_units,out_units,freq,sps

def convert_units(in_units,value):
    # assume in_units m/s, m and out_units COUNTS
    # so value * COUNTS = m/s 
    if in_units.lower() == 'm/s':
        value=1/(value/1e9)
        in_units = 'nm/s'
    if in_units.lower() == 'm':
        value=1/(value/1e9)
        in_units = 'nm'
    return in_units,value

def find_flatband2(resp,sens):
    # perferred method to find flat band (for now)
    amps=np.abs(resp)
    deriv=np.diff(amps) # take the 1st derivate of the amplitude responce
    mean=deriv.mean() 
    std=deriv.std() 
    print(f'Flatband mean:{mean} std:{std}')
    flat_ind=(deriv>=mean-std) & (deriv<= mean+std) # find the indexs which are within 1-sigma of the mean
    idx,=flat_ind.nonzero() # All idx where above is True
    print(len(flat_ind),len(idx))
    # find the consecutive seqments 
    start_indx=idx[0]
    i=start_indx
    continuous_segs=[] # holder array for 
    for n,j in enumerate(idx[1:]):
        if j-i > 1: # if there's a gap > 1 in consecutive indexes, then we found a seqment
            end_indx=i
            continuous_segs.append([start_indx,end_indx])
            start_indx=j
        i=j
    # find the longest segment
    rng=0
    keep=-1
    print(len(continuous_segs))
    if len(continuous_segs) > 0:
        for n,i in enumerate(continuous_segs):
            rng_cur=i[1]-i[0]
            if rng_cur > rng:
                keep=n
                rng=rng_cur
    else:
        print('find_flatband failed')
    if keep >=0:
        low_corner=continuous_segs[keep][0]
        high_corner=continuous_segs[keep][1]
    else:
        low_corner=None
        high_corner=None
    return low_corner,high_corner


def find_flatband(resp,sens):
    amps=np.abs(resp)/sens
    flat_ind=(amps>=0.95) & (amps<= 1.05)
    low_corner=-1
    high_corner=-1
    seg=False
    for i in range(len(flat_ind)): # find first segment that meets conditions 
        if flat_ind[i] == True and low_corner < 0: 
            low_corner=i
            seg=True
        if seg and not flat_ind[i]: # when true -> false, stop
            high_corner=i
            seg=False
            break
    return low_corner,high_corner,

def plot_response(info):
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.use('Agg')
    from matplotlib.ticker import FuncFormatter

    # set up figure
    fig = plt.figure(figsize=(7, 10),dpi=200)
    gs=fig.add_gridspec(3,1)
    gs.update(wspace=0.05, hspace=0.10)
    color={"color": "0.7"}

    # stuff to plot
    amplitude=np.abs(info['resp'])/info['value']
    freqs=info['freqs']
    xmin=freqs[0]
    xmax=freqs[-1]

    # plot Response
    ax1=fig.add_subplot(gs[0,0])
    ax1.loglog(freqs,amplitude,linewidth=2,color='black')
    minmax=ax1.get_ylim()
    ax1.set_xlim(xmin,xmax)
    ax1.set_ylim(amplitude[0]*.1,minmax[1])

    # find low freq corner
    lowc,highc=find_flatband2(info['resp'],info['value'])
    if not lowc and not highc:
        lowc,highc=find_flatband(info['resp'],info['value'])
    try:
        lowcf=info['freqs'][lowc]
        highcf=info['freqs'][highc]
    except Exception as e:
        print(f'problem with flatband\n\t{e}')
        lowcf=0
        highcf=0
        pass;


    # add lines to plot
    ax1.axvline(x=lowcf,ymin=0,ymax=1)
    ax1.axvline(x=highcf,ymin=0,ymax=1)
    # add text
    txt=f"{lowcf:0.3f} Hz"
    ax1.text(x=lowcf,y=amplitude[0],s=txt,fontsize=8,ha='center',va='top',
        bbox=dict(facecolor='white', edgecolor='black'))
    txt=f"{highcf:0.3f} Hz"
    ax1.text(x=highcf,y=amplitude[0],s=txt,fontsize=8,ha='center',va='top',
        bbox=dict(facecolor='white', edgecolor='black'))

    # make things look good
    formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y))
    ax1.xaxis.set_major_formatter(formatter)
    ax1.xaxis.grid(b=True, which="major", **color)
    ax1.yaxis.grid(b=True, which="major", **color)
    ax1.set_ylabel('Amplitude') 
    ax1.set_title(info['SEEDid'],fontsize=12)


    # Plot phase
    ax2=fig.add_subplot(gs[1,0],sharex=ax1)
    ax2.semilogx()
    ax2.plot(info['freqs'],np.angle(info['resp'],deg=False),linewidth=2,color='black')
    # make pretty labels
    minmax2 = ax2.yaxis.get_data_interval()
    yticks2 = np.arange(minmax2[0] - minmax2[0] % (np.pi / 2),
        minmax2[1] - minmax2[1] % (np.pi / 2) + np.pi, np.pi / 2)
    ax2.set_yticks(yticks2)
    ax2.set_yticklabels([_pitick2latex(x) for x in yticks2])
    ax2.xaxis.set_major_formatter(formatter)
    ax2.xaxis.grid(b=True, which="major", **color)
    ax2.yaxis.grid(b=True, which="major", **color)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase [rad]')

    # legend
    pos1 = ax2.get_position()
    newax=[pos1.x0, pos1.y0,
        pos1.width*.58,pos1.height*.35]
    fig=ax2.get_figure()
    ax4=fig.add_axes(newax)
    ax4.patch.set_facecolor('lightgray')
    ax4.patch.set_alpha(0.8)
    ax4.xaxis.set_visible(False)
    ax4.yaxis.set_visible(False)
    ax4.set_xlim(0,10)
    ax4.set_ylim(0,10)

    in_units,value=convert_units(info['in_units'],info['value'])
    txt=f"ncalib: {value:16.9g} x counts = {in_units}"
    ax4.text(x=0.4, y=8,s=txt, ha="left",fontsize=10)
    txt=f"ncalib evaluated at {info['freq']} Hz"
    ax4.text(x=0.4, y=6,s=txt, ha="left",fontsize=10)
    txt=f'Flatband $(\pm 1\sigma)$: {lowcf:0.3f} - {highcf:0.3f} Hz'
#    txt+=r"$ (\pm 5 \%)$"
    ax4.text(x=.4, y=4,s=txt, ha="left",fontsize=10)
    txt=f"Nyquist: {info['sps']/2:0.2f} Hz"
    ax4.text(x=.4, y=2,s=txt, ha="left",fontsize=10)

    info['value']=value
    info['in_units']=in_units
    plt.savefig(info['outpng'],bbox_inches='tight')
    return info

def main():
    parser = argparse.ArgumentParser(prog=progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=
            'Report Sensitivities from a StaXML file with response info. And plot response.')

    parser.add_argument("-i","--staxml", type=str,
        required=True, help="Name of the station xml file")

    parser.add_argument("-s","--SEEDid", type=str,
        required=False, help="Seed ID to process (Net.Station.LocationCode.Chan). Leave blank to get a list of all available in StaXML file")

    parser.add_argument("-r","--report", action='store_true',default=False,
        required=False, help="No plotting just report info")

    parser.add_argument("--recalculate_sensitivity",action='store_true',default=False,
        required=False, help="Recalculate overall sensitivity and save new staxml")

    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")

    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    inv_name=args.staxml
    debug=args.verbose
    recalc=args.recalculate_sensitivity
    inv=read_inventory(inv_name)
    if not args.SEEDid:
        print_stas(inv)
        sys.exit(0)

    net,sta,loc,chan=args.SEEDid.split(".")
    msg=f"network:{net} sta:{sta} loc:{loc} chan:{chan}"
    print(msg)

    info={}
    stainv=inv.select(network=net,station=sta,location=loc,channel=chan)
    if recalc:
        print("Recalculating sensitivities")
        for net in stainv:
            for sta in net.stations:
                for chan in sta.channels:
                    print(f"Response before ..............\n{chan.response}\n")
                    chan.response.recalculate_overall_sensitivity(frequency=12.0)
                    print(f"Response after ...............\n{chan.response}\n")
                    chan.response.recalculate_overall_sensitivity(frequency=12.0)
                    print(f"Response after ...............\n{chan.response}\n")
        inv.write(f"{inv_name}.new",format="STATIONXML")
       
    info['freqs'],info['resp'],info['value'],info['in_units'],info['out_units'],info['freq'],info['sps']=get_response(stainv)
    info['outpng']=f"{args.SEEDid}.response.png"
    info['SEEDid']=args.SEEDid
    if not args.report:
        info=plot_response(info)
    else:
        in_units,value=convert_units(info['in_units'],info['value'])
        msg=f"{args.SEEDid} Sensitivity: {value:16.9g} (Convert {info['out_units']} to {in_units})"
        print(msg)

if __name__ == '__main__':
    main()

