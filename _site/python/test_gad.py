
import subprocess, os, emoji, random, pandas

platformlist = ['GPL13534','GPL21145', 'GPL570', 'GPL10558', 'GPL96']

datapath=os.path.join('inst', 'data'); metadf_name='arraymetadf.csv'
queriespath=os.path.join('inst', 'queries')
datapath=os.path.join('inst', 'data'); metadf_name='arraymetadf.csv'
metadf_path=os.path.join(datapath, metadf_name)
metadf=pandas.read_csv(metadf_path, sep = ',', header=0)

print("Performing new GEO query..."); rl = {}
for platform in platformlist:
    print("Beginning queries for platform " + platform); rl[platform]={}
    # all studies (GSE IDs)
    args_gse = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gse[ETYP] AND Homo sapiens[ORGN]'"])
    output_gse=subprocess.check_output(args_gse, shell=True)
    output_gse=str(output_gse)
    rl[platform]["gse"]=output_gse.split('<Count>')[1].split('</Count>')[0]
    # all samples (GSM IDs)
    args_gsm = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gsm[ETYP] AND Homo sapiens[ORGN]'"])
    output_gsm=subprocess.check_output(args_gsm, shell=True)
    output_gsm=str(output_gsm)
    rl[platform]["gsm"]=output_gsm.split('<Count>')[1].split('</Count>')[0]
    ptype=metadf.type[metadf.accession==platform].item()
    # for dnam type, also check supplement with `idat[suppFile]`
    if ptype=="DNAm":
        print("Detecting IDATs for platform " + platform)
        # studies with IDATs
        args_gse_idat = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gse[ETYP] AND Homo sapiens[ORGN] AND idat[suppFile]'"])
        output_gse_idat=subprocess.check_output(args_gse_idat, shell=True)
        output_gse_idat=str(output_gse_idat)
        rl[platform]["gse_idat"]=output_gse_idat.split('<Count>')[1].split('</Count>')[0]
        # samples with IDATs
        args_gsm_idat = ''.join(["esearch -db gds -query '", platform,
        "[ACCN] AND gsm[ETYP] AND Homo sapiens[ORGN] AND idat[suppFile]'"])
        output_gsm_idat=subprocess.check_output(args_gsm_idat, shell=True)
        output_gsm_idat=str(output_gsm_idat)
        rl[platform]["gsm_idat"]=output_gsm_idat.split('<Count>')[1].split('</Count>')[0]
    print("Finished queries for platform " + platform)

    return rl



lnumarray_gsm = [rl[list(rl)[i]]["gsm"] for i in range(0,len(rl))]
lnumarray_gse = [rl[list(rl)[i]]["gse"] for i in range(0,len(rl))]
laccarray = [i for i in metadf.accession]
ltypearray = [i for i in metadf.type]
laliasshort = [i for i in metadf.alias_short]

lnumarray = lnumarray_gsm; charlim=280
lexpr = ["neat", "wow", "whoa", "check it out"]
lemojis=[':computer:', ':bulb:', ':chart_with_upwards_trend:', ':bar_chart:',
    ':microscope:', ':newspaper:', ':calendar:', ':hourglass:']
ltags=['#ncbi', '#biomedicine', '#reproducibleresearch', '#publicdata',
    '#bioinformatics', '#computationalbiology', '#GEO', '#geoarraydigest',
    '#biotechnology', '#arraydata', '#microarray', '#geneexpression', 
    '#genomics', '#dnamethylation', '#epigenetics']

arrtxt = [
        str(lnumarray[i]) + ' GSMs for acc ' + 
        str(laccarray[i]) + ' (type: ' + str(ltypearray[i]) + 
        ', alias: ' + laliasshort[i] + ')'
        for i in range(0, len(lnumarray)-2)
]
arrtxt = ', '.join(arrtxt[0:-1]) + ', and ' + arrtxt[-1]
newtxt = ' '.join([
        'I just found', arrtxt + 
        ' in GEO!'
])
# randomized beginning expressions
rexpr=random.choices(lexpr)[0]+"!";rexpr=rexpr[0].capitalize()+rexpr[1::]
newtxt=' '.join([rexpr, newtxt])
# pick 2 emojis and tags, up to character limit
if len(newtxt) < charlim: 
    random.shuffle(lemojis); random.shuffle(ltags)
    remoji=' '.join([emoji.emojize(i, use_aliases=True) 
                for i in lemojis[0:3]
            ])
    rtags=' '.join([i for i in ltags[0:3]])
    newmsg=' '.join([newtxt, rtags, remoji])
else:
    newmsg=newtxt
return newmsg






