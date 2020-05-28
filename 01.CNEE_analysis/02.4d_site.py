#!/usr/env/python

import re
import sys
import os

inf=open('01.maf-file.list')
out=open('03.get_4d_site.sh','w')
os.system('rm -rf 4d_sites')
os.mkdir('4d_sites')
for line in inf:
	l=line.strip()
	aa=line.split('/')[-1].strip().replace('.sing.maf','')
	bb=line.split('/')[-1].strip()
	chrname=aa.replace('goat.','')
	out.write('cd /public/home/liuchang/projects/giraffe/01.HCE ;./bin/msa_view '+l+' --in-format MAF --4d --features goat_ensemble/gff/'+chrname+'.gff.sort.gff >4d_sites/'+bb+'.codon.ss\n')

inf.close()
out.close()
