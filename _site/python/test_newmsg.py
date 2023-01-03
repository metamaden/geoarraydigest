#!/usr/bin/env python

# Author: Sean Maden
# Script to text the automated text generation for new tweets.

import emoji, random

charlim=280

lexpr=[
    "neat",
    "wow",
    "whoa",
    "check it out"
]

lemojis=[
    ':computer:',
    ':bulb:',
    ':chart_with_upwards_trend:',
    ':bar_chart:',
    ':microscope:',
    ':newspaper:',
    ':calendar:',
    ':hourglass:'
]

ltags=[
    '#ncbi',
    '#biomedicine',
    '#reproducibleresearch',
    '#publicdata',
    '#bioinformatics',
    '#computationalbiology',
    '#GEO',
    '#geoarraydigest',
    '#biotechnology',
    '#arraydata',
    '#microarray',
    '#geneexpression',
    '#genomics',
    '#dnamethylation',
    '#epigenetics'
]

# Get new message
lnumarray=[1234, 567]; ltypearray=["A", "B"]; laliasarray=["HM450K", "EPIC"]

arrtxt = [
    str(lnumarray[i]) + ' samples for platform ' + 
    str(ltypearray[i]) + ' (' + str(laliasarray[i]) + ')'
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