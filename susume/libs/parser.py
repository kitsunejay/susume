#!python
from pprint import pprint


### Requires raw strings to work properly ###
string = r"DEF:146 HP+74 MP+99 STR+31\\nDEX+31 VIT+31 AGI+31\\nINT+39 MND+45 CHR+39\\nAccuracy+40 Attack+65\\nMagic Accuracy+40\\nEvasion+61 Magic Evasion+100\\n\\\"Magic Def. Bonus\\\"+8\\nHealing magic skill +23\\nEnhancing magic skill +23\\nHaste+3% \\\"Fast Cast\\\"+15%\\nEnhancing magic duration +15%"
#string = r"DEF:133 HP+80 STR+24 DEX+25 VIT+21\\nAGI+25 INT+24 MND+24 CHR+24 Accuracy+21 Attack+21\\nEvasion+52 Magic Evasion+53\\n\\\"Magic Def. Bonus\\\"+4 Haste+4%\\nAutomaton: Accuracy+21\\nRanged Accuracy+21 \\\"Store TP\\\"+13"
#string = r"DMG:216 Delay:480 Accuracy+25\\nGreat Sword skill +242\\nParrying skill +242\\nMagic Accuracy skill +188\\nOccasionally attacks twice\\nAdditional effect: Haste"

# Split on newline
sstring = string.split("\\\\n")
nstring = []

# Scrub escape'd special characters
for s in sstring:
    nstring.append(s.replace("\\",""))

for i in range(len(nstring)):
    print("[{}]\t>  {}".format(i,nstring[i]))
