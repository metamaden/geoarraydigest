#!/usr/bin/env python

import subprocess
import os

""" gadbqueries.py

Author: Sean Maden

Get tables of available samples (GSM IDs) and studies (GSE IDs) from
the Gene Expression Omnibus (GEO). Functions use equery from the Entrez Programming 
Utilities software (url: https://www.ncbi.nlm.nih.gov/books/NBK179288/).

"""

def gsm_eqtable(startdate=2000,enddate=2018, platformlist = ['GPL13534','GPL21145'],
    tablename='gsmyeardata', writetable=True):
    """ Human sample counts on methylation array platforms, over year range
        From GEO via equery, fetch sample counts on methylation array platforms
            over a range of years.
        Arguments
            * startdate : start of publication date range to search
            * enddate : end of publication date range to search
            * platformlist : methylation array platforms to search
            * tablename : name of data table to write
            * writetable : whether to write results into data table
        Returns
            * rl (list) : list of results (by platform-year), optionally writing
                new data table as side effect
    """
    yearrange = list(range(startdate-1,enddate+1))  
    rl = []
    for platform in platformlist:
        for year in yearrange:
            fn = platform+"_"+str(year)
            subp_strlist1 = ["esearch","-db","gds","-query",
                "".join(["'",
                    platform,
                    "[ACCN] AND gsm[ETYP] AND ",
                    str(year),
                    "[PDAT] AND Homo sapiens[ORGN]'"])
                ]
            subp_strlist2 = ["efetch","-format","docsum"]
            subp_strlist3 = ["xtract","-pattern","DocumentSummary",
                "-element","Id Accession",">",fn]
            args = " | ".join([" ".join(subp_strlist1),
                " ".join(subp_strlist2),
                " ".join(subp_strlist3)])
            output=subprocess.check_output(args, shell=True)
            resultlist = [line.rstrip('\n') for line in open(fn)]
            # use set to grab number of unique ids in the file
            rl.append([platform,year,str(len(set(resultlist)))])
            os.remove(fn)
    # write results to readable table
    if writetable:
        with open(tablename,'w') as d:
            for line in rl:
                d.write(" ".join([str(k) for k in line])+"\n")
    return rl

def gse_eqtable(startdate=2000,enddate=2018,tablename='gseyeardata',
    platformlist = ['GPL13534','GPL21145'], writetable=True):
    """ Human experiment counts on methylation array platforms, over year range
        From GEO via equery, fetch experiment counts on methylation array 
            platforms over a range of years.
        Arguments
            * startdate : start of publication date range to search
            * enddate : end of publication date range to search
            * platformlist : methylation array platforms to search
            * tablename : name of data table to write
            * writetable : whether to write results into data table
        Returns
            * rl (list) : list of results (by platform-year), optionally writing
                new data table as side effect
    """
    yearrange = list(range(startdate-1,enddate+1))  
    rl = []
    for platform in platformlist:
        for year in yearrange:
            fn = platform+"_"+str(year)
            subp_strlist1 = ["esearch","-db","gds","-query",
                "".join(["'",
                    platform,
                    "[ACCN] AND gse[ETYP] AND ",
                    str(year),
                    "[PDAT]'"])
                ]
            subp_strlist2 = ["efetch","-format","docsum"]
            subp_strlist3 = ["xtract","-pattern","DocumentSummary",
                "-element","Id Accession",">",fn]
            args = " | ".join([" ".join(subp_strlist1),
                " ".join(subp_strlist2),
                " ".join(subp_strlist3)])
            output=subprocess.check_output(args, shell=True)
            resultlist = [line.rstrip('\n') for line in open(fn)]
            # use set to grab number of unique ids in the file
            rl.append([platform,year,str(len(set(resultlist)))])
            os.remove(fn)
    # write results to readable table
    if writetable:
        with open(tablename,'w') as d:
            for line in rl:
                d.write(" ".join([str(k) for k in line])+"\n")
    return rl

def gsmidat_eqtable(startdate=2000,enddate=2018,
    platformlist = ['GPL13534','GPL8490','GPL21145'],tablename='gsmidatyrdat',
    writetable=True):
    """ Human gsm idat counts on methylation array platforms, over year range
        From GEO via equery, fetch experiment counts on methylation array 
            platforms over a range of years.
        Arguments
            * startdate : start of publication date range to search
            * enddate : end of publication date range to search
            * platformlist : methylation array platforms to search
            * tablename : name of data table to write
            * writetable : whether to write results into data table
        Returns
            * rl (list) : list of results (by platform-year), optionally writing
                new data table as side effect
    """
    yearrange = list(range(startdate-1,enddate+1))  
    rl = []
    for platform in platformlist:
        for year in yearrange:
            fn = platform+"_"+str(year)
            subp_strlist1 = ["esearch","-db","gds","-query",
                "".join(["'",
                    platform,
                    "[ACCN] AND idat[suppFile] AND gsm[ETYP]",
                    str(year),
                    "[PDAT] AND Homo sapiens[ORGN]'"])
                ]
            subp_strlist2 = ["efetch","-format","docsum"]
            subp_strlist3 = ["xtract","-pattern","DocumentSummary",
                "-element","Id Accession",">",fn]
            args = " | ".join([" ".join(subp_strlist1),
                " ".join(subp_strlist2),
                " ".join(subp_strlist3)])
            output=subprocess.check_output(args, shell=True)
            resultlist = [line.rstrip('\n') for line in open(fn)]
            # use set to grab number of unique ids in the file
            rl.append([platform,year,str(len(set(resultlist)))])
            os.remove(fn)
    # write results to readable table
    if writetable:
        with open(tablename,'w') as d:
            for line in rl:
                d.write(" ".join([str(k) for k in line])+"\n")
    return rl

def gseidat_eqtable(startdate=2000,enddate=2018, platformlist = ['GPL13534','GPL21145'],
    tablename='gseidatyrdat', writetable=True):
    """ Human gse idat counts on methylation array platforms, over year range
        From GEO via equery, fetch experiment counts on methylation array 
            platforms over a range of years.
        Arguments
            * startdate : start of publication date range to search
            * enddate : end of publication date range to search
            * platformlist : methylation array platforms to search
            * tablename : name of data table to write
            * writetable : whether to write results into data table
        Returns
            * rl (list) : list of results (by platform-year), optionally writing
                new data table as side effect
    """
    yearrange = list(range(startdate-1,enddate+1))  
    rl = []
    for platform in platformlist:
        for year in yearrange:
            fn = platform+"_"+str(year)
            subp_strlist1 = ["esearch","-db","gds","-query",
                "".join(["'",
                    platform,
                    "[ACCN] AND idat[suppFile] AND gse[ETYP]",
                    str(year),
                    "[PDAT] AND Homo sapiens[ORGN]'"])
                ]
            subp_strlist2 = ["efetch","-format","docsum"]
            subp_strlist3 = ["xtract","-pattern","DocumentSummary",
                "-element","Id Accession",">",fn]
            args = " | ".join([" ".join(subp_strlist1),
                " ".join(subp_strlist2),
                " ".join(subp_strlist3)])
            output=subprocess.check_output(args, shell=True)
            resultlist = [line.rstrip('\n') for line in open(fn)]
            # use set to grab number of unique ids in the file
            rl.append([platform,year,str(len(set(resultlist)))])
            os.remove(fn)
    # write results to readable table
    if writetable:
        with open(tablename,'w') as d:
            for line in rl:
                d.write(" ".join([str(k) for k in line])+"\n")
    return rl

if __name__ == "__main__":
    """ Generate tables of available samples and studies
    """
    gsm_eqtable()
    gse_eqtable()
    gsmidat_eqtable()
    gseidat_eqtable()