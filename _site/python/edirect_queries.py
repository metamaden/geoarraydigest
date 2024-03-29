#!/usr/bin/env python

""" edirect_queries.py

Author: Sean Maden

"""

import subprocess, os, pandas
from datetime import date

def new_digest(platformlist = ['GPL13534','GPL21145', 'GPL570', 'GPL10558', 'GPL96'],
	datapath=os.path.join('data'), metadf_name='arraymetadf.csv',
	queriespath=os.path.join('inst', 'queries'), totalsdir='totals'):
	""" run_gad

	Main function to assemble a new GEO array digest.

	"""
	print("Making new digest...")
	print("Parsing array metadata df...")
	metadf_path=os.path.join(datapath, metadf_name)
	metadf=pandas.read_csv(metadf_path, sep = ',', header=0)
	print("Querying the GDS API...")
	dig = get_esearch_rl(platformlist, metadf)
	print("Writing query results to data table...")
	datestr = date.today().strftime("%Y-%m-%d")
	write_data(dig, metadf, datestr)
	print("Writing new post...")
	write_post(dig, metadf, datestr)
	print("Returning query results...")
	return dig

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
		if cond.bool():
			print("Detecting IDATs for platform " + platform); rl[platform]["gse_idat"]={}
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

def write_data(dig, metadf, datestr, datapath = os.path.join("data"),
	colnames=["platform_id", "data_type", "alias_short", 
	"release_date", "geo_id_type", "num_records\n"]):
	"""
	"""
	newdata_fname="data_"+datestr+".csv"
	newdata_fpath=os.path.join(datapath, newdata_fname)
	print("Writing data to CSV: `"+newdata_fpath+"`...")
	with open(newdata_fpath, "w") as of:
		of.write(",".join(colnames))
		for key1 in dig.keys():
			col1 = key1
			col2 = metadf.type[metadf.accession==col1].tolist()[0]
			col3 = metadf.alias_short[metadf.accession==col1].tolist()[0]
			col4 = metadf.release_date[metadf.accession==col1].tolist()[0]
			for key2 in dig[key1].keys():
				col5 = key2
				col6 = dig[key1][key2]
				of.write(",".join([col1,col2,col3,col4,col5,col6+"\n"]))
	of.close()
	return True

def write_post(dig, metadf, datestr, postpath = os.path.join("_posts")):
	"""
	"""
	newpost_fname = datestr+"-Array-Digest.MARKUP"
	newpost_fpath = os.path.join(postpath, newpost_fname)
	print("Writing data to post: `"+newpost_fpath+"`...")
	with open(newpost_fpath, "w") as of:
		of.write("---\n")
		of.write("layout: post\n")
		of.write("title: "+datestr+" Array Digest\n")
		of.write("---\n")
		for accid in dig.keys():
			digacc = dig[accid]
			alias = metadf.alias_short[metadf.accession==accid].tolist()[0]
			newline = "".join(
			[
				"For platform ",accid," (",alias,"), found ",
				digacc['gse']," studies and ",
				digacc['gsm']," samples."
			]
			)
			cond = metadf.type[metadf.accession==accid]=="DNAm"
			if cond.bool():
				newline = "".join(
				[
					newline,". Of these, ",digacc['gse_idat']," studies and ",
					digacc['gsm_idat']," samples have IDATs."
				]
				)
			of.write(newline+"\n\n")
	of.close()
	return True


if __name__ == "__main__":
    """ Generate tables of available samples and studies
    """
    new_digest()