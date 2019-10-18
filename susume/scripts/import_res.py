#python 
import sys
import argparse
#from slpp import slpp
import re

parser = argparse.ArgumentParser(description='Import res files from Windower4')
parser.add_argument('--file','-f', dest='resfile',
                    help='tbd')

args = parser.parse_args()

if args.resfile:
    print("Reading [%s]:\n" % args.resfile)
else:
    print("No file specified. Please use -f argument")
    sys.exit(1)
with open(args.resfile,'r',encoding="utf8") as rf:
    lines = rf.readlines()
    #print(lines[1:5])
    #for i in lines:
    print(lines[2].strip('\n'))
    #slpp.decode(lines[1:5])