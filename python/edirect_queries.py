#!/usr/bin/env python

""" gadbqueries.py

Author: Sean Maden

"""

import subprocess, os, pandas

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
		print(cond)
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

if __name__ == "__main__":
    """ Generate tables of available samples and studies
    """
    print("Beginning new API query...")
    run_gad()