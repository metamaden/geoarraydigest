#!/usr/bin/env python

""" gadbqueries.py

Author: Sean Maden

First, get tables of available samples (GSM IDs) and studies (GSE IDs) from
the Gene Expression Omnibus (GEO). Functions use equery from the Entrez Programming 
Utilities software (url: https://www.ncbi.nlm.nih.gov/books/NBK179288/).

Next, generate the automated tweet message with randomized generation of 
start expressions and terminal emojis and tags. Finally, submit the new message 
to Twitter's API using the `twurl` app.

Functions:

* make_newmsg: 
* submit_tweet: 

"""

import subprocess, os, emoji, random, pandas

platformlist = ['GPL13534','GPL21145', 'GPL570', 'GPL10558', 'GPL96']
datapath=os.path.join('inst', 'data')
metadf_name='arraymetadf.csv'
queriespath=os.path.join('inst', 'queries')
totalsdir='totals'
print("Parsing array metadata df...")
datapath=os.path.join('inst', 'data'); metadf_name='arraymetadf.csv'
metadf_path=os.path.join(datapath, metadf_name)
metadf=pandas.read_csv(metadf_path, sep = ',', header=0)
# rl = get_esearch_rl(platformlist, metadf)

print("Performing new GEO query..."); rl = {}
for ii,platform in enumerate(platformlist):
    print("Beginning queries for platform " + platform); rl[platform]={}
    args_gse = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gse[ETYP] AND Homo sapiens[ORGN]'"])
    output_gse=subprocess.check_output(args_gse, shell=True)
    output_gse=str(output_gse)
    rl[platform]["gse"]=output_gse.split('<Count>')[1].split('</Count>')[0]
    args_gsm = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gsm[ETYP] AND Homo sapiens[ORGN]'"])
    output_gsm=subprocess.check_output(args_gsm, shell=True)
    output_gsm=str(output_gsm)
    rl[platform]["gsm"]=output_gsm.split('<Count>')[1].split('</Count>')[0]
    cond=metadf.type[metadf.accession==platform]=="DNAm"
    if cond[ii]:
        print("Detecting IDATs for platform " + platform)
        args_gse_idat = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gse[ETYP] AND Homo sapiens[ORGN] AND idat[suppFile]'"])
        output_gse_idat=subprocess.check_output(args_gse_idat, shell=True)
        output_gse_idat=str(output_gse_idat)
        rl[platform]["gse_idat"]=output_gse_idat.split('<Count>')[1].split('</Count>')[0]
        args_gsm_idat = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gsm[ETYP] AND Homo sapiens[ORGN] AND idat[suppFile]'"])
        output_gsm_idat=subprocess.check_output(args_gsm_idat, shell=True)
        output_gsm_idat=str(output_gsm_idat)
        rl[platform]["gsm_idat"]=output_gsm_idat.split('<Count>')[1].split('</Count>')[0]
    print("Finished queries for platform " + platform)

lnumarray=[v["gsm"] for v in rl.values()]
ltypearray=[t for t in metadf.type]
laliasarray=[a for a in metadf.alias_short]
charlim=280

lexpr = ["neat", "wow", "whoa", "check it out"] 
lemojis=[':computer:', ':bulb:', ':chart_with_upwards_trend:', ':bar_chart:',
            ':microscope:', ':newspaper:', ':calendar:', ':hourglass:'
        ]
ltags=['#ncbi', '#biomedicine', '#reproducibleresearch', '#publicdata',
        '#bioinformatics', '#computationalbiology', '#GEO', '#geoarraydigest',
        '#biotechnology', '#arraydata', '#microarray', '#geneexpression', 
        '#genomics', '#dnamethylation', '#epigenetics'
        ]
arrtxt = [str(lnumarray[i]) + ' samples for platform ' + 
            str(ltypearray[i]) + ' (alias: ' + str(laliasarray[i]) + 
            ', type: ' + str(ltypearray[i]) + ')'
            for i in range(3)
        ]
arrtxt = ', '.join(arrtxt[0:-1]) + ', and ' + arrtxt[-1]
newtxt = ' '.join(['I just found', arrtxt + 
                    ' in the GEO db!'
                ])
# randomized beginning expressions
rexpr=random.choices(lexpr)[0]+"!";rexpr=rexpr[0].capitalize()+rexpr[1::]
newtxt=' '.join([rexpr, newtxt])
# pick 2 emojis and tags, up to character limit
if len(newtxt) < charlim-10: 
    remoji=' '.join([emoji.emojize(i, use_aliases=True) 
                for i in random.choices(lemojis, k=3)
            ])
    rtags=' '.join([i for i in random.choices(ltags, k=3)])
    newmsg=' '.join([newtxt, rtags, remoji])
else:
    newmsg=newtxt

ll=['twurl', '-d', "'" + newmsg + "'", '/1.1/statuses/update.json']
spl=' '.join(ll)
output=subprocess.check_output(spl, shell=True)


twurl -d 'status=Check it out! I just found 107988 samples for platform DNAm (alias: HM450K, type: DNAm), 26432 samples for platform DNAm (alias: EPIC, type: DNAm), and 161114 samples for platform expr (alias: U133_v2, type: expr) in the GEO db! #biomedicine #geneexpression #GEO 📊 📈 📰' /1.1/statuses/update.json

def run_gad(platformlist = ['GPL13534','GPL21145', 'GPL570', 'GPL10558', 'GPL96'],
    datapath=os.path.join('inst', 'data'), metadf_name='arraymetadf.csv',
    queriespath=os.path.join('inst', 'queries'), totalsdir='totals'):
    """ run_gad

    Main function to assemble a new GEO array digest.
    
    """
print("Parsing array metadata df...")
datapath=os.path.join('inst', 'data'); metadf_name='arraymetadf.csv'
metadf_path=os.path.join(datapath, metadf_name)
metadf=pandas.read_csv(metadf_path, sep = ',', header=0)
rl = get_esearch_rl(platformlist, metadf)
    # make new message
    # submit new tweet
    return None

def get_esearch_rl(platformlist, metadf):
    """ get_esearch_rl
    
    Get array info from GEO API using Entrez Direct Utilities.

    """
print("Performing new GEO query..."); rl = {}
for platform in platformlist:
print("Beginning queries for platform " + platform); rl[platform]={}
args_gse = ''.join(["esearch -db gds -query '", platform,
    "[ACCN] AND gse[ETYP] AND Homo sapiens[ORGN]'"])
output_gse=subprocess.check_output(args_gse, shell=True)
output_gse=str(output_gse)
rl[platform]["gse"]=output_gse.split('<Count>')[1].split('</Count>')[0]
args_gsm = ''.join(["esearch -db gds -query '", platform,
    "[ACCN] AND gsm[ETYP] AND Homo sapiens[ORGN]'"])
output_gsm=subprocess.check_output(args_gsm, shell=True)
output_gsm=str(output_gsm)
rl[platform]["gsm"]=output_gsm.split('<Count>')[1].split('</Count>')[0]
cond=metadf.type[metadf.accession==platform]=="DNAm"
    if cond[0]:
        print("Detecting IDATs for platform " + platform)
        args_gse_idat = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gse[ETYP] AND Homo sapiens[ORGN] AND idat[suppFile]'"])
        output_gse_idat=subprocess.check_output(args_gse_idat, shell=True)
        output_gse_idat=str(output_gse_idat)
        rl[platform]["gse_idat"]=output_gse_idat.split('<Count>')[1].split('</Count>')[0]
        args_gsm_idat = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gsm[ETYP] AND Homo sapiens[ORGN] AND idat[suppFile]'"])
        output_gsm_idat=subprocess.check_output(args_gsm_idat, shell=True)
        output_gsm_idat=str(output_gsm_idat)
        rl[platform]["gsm_idat"]=output_gsm_idat.split('<Count>')[1].split('</Count>')[0]
        print("Finished queries for platform " + platform)
    return rl

def make_newmsg(lnumarray, ltypearray, laliasarray, charlim=280,
    lexpr = ["neat", "wow", "whoa", "check it out"], 
    lemojis=[':computer:', ':bulb:', ':chart_with_upwards_trend:', ':bar_chart:',
    ':microscope:', ':newspaper:', ':calendar:', ':hourglass:'],
    ltags=['#ncbi', '#biomedicine', '#reproducibleresearch', '#publicdata',
    '#bioinformatics', '#computationalbiology', '#GEO', '#geoarraydigest',
    '#biotechnology', '#arraydata', '#microarray', '#geneexpression', 
    '#genomics', '#dnamethylation', '#epigenetics']
    ):
    """ Get the automated message text for a new tweet, with randomization
    
    Arguments

    Returns
        newmsg: Text containing the array summary stats with randomized 
            expression, emojis, and tags.

    """
    arrtxt = [
        str(lnumarray[i]) + ' samples for platform ' + 
        str(ltypearray[i]) + ' (alias: ' + str(laliasarray[i]) + 
        ', type: ' + str(ltypearray[i]) + ')'
        for i in range(len(lnumarray))
    ]
    arrtxt = ', '.join(arrtxt[0:-1]) + ', and ' + arrtxt[-1]
    newtxt = ' '.join([
            'I just found', arrtxt + 
            ' in the GEO db! https://www.ncbi.nlm.nih.gov/geo/'
    ])
    # randomized beginning expressions
    rexpr=random.choices(lexpr)[0]+"!";rexpr=rexpr[0].capitalize()+rexpr[1::]
    newtxt=' '.join([rexpr, newtxt])
    # pick 2 emojis and tags, up to character limit
    if len(newmsg) < charlim: 
        remoji=' '.join([emoji.emojize(i, use_aliases=True) 
                    for i in random.choices(lemojis, k=3)
                ])
        rtags=' '.join([i for i in random.choices(ltags, k=3)])
        newmsg=' '.join([newtxt, rtags, remoji])
    else:
        newmsg=newtxt
    return newmsg

def submit_tweet(newmsg):
    """ Submit the new tweet using `twurl`
    """
    ll=[
        'twurl', '-d', 
        newmsg, 
        '/1.1/statuses/update.json'
    ]; spl=' '.join(ll)
    output=subprocess.check_output(spl, shell=True)
    return output

if __name__ == "__main__":
    """ Generate tables of available samples and studies
    """
    #"twurl -d 'status=" + newmsg + "'" + " /1.1/statuses/update.json" 
    #twurl -d 'status=Neat! I just found 107039 GSMs for acc GPL13534 (type: DNAm, alias: HM450K), 25130 GSMs for acc GPL21145 (type: DNAm, alias: EPIC), and 160861 GSMs for acc GPL570 (type: expr, alias: U133_v2) in GEO! #genomics #dnamethylation #biotechnology 🔬 ⌛ 📆' /1.1/statuses/update.json
    print("Beginning new API query...")
    run_gad()
    get_esearch_rl()
    print("Making new tweet...")
    newmsg = make_newmsg()
    submit_tweet(newmsg)
    print("Finished submitting new tweet.")