#!python
import os
import platform
from slpp import slpp as lua
import json
from pprint import pprint
import requests

######################################

local_url = 'http://localhost:8000/susume/'

######################################



def get_resource(path):
    if platform.system() == 'Windows':
        path = 'C:\\Program Files (x86)\\Windower4\\res\\' + path
    with open(path, encoding="utf8") as fd:
        data = fd.read().replace('return', '', 1)
        return lua.decode(data)

'''
res_jobs = get_resource('jobs.lua')

#print(len(items.keys()))
#print(type(items))


jobs_json = []

for k in res_jobs.keys():
    print("{}={}".format(k,res_jobs[k]))
    jobs_json.append(res_jobs[k])
for k in res_jobs.keys():
    print("{},{}".format(res_jobs[k]['en'],res_jobs[k]['ens']))

#print(jobs_json)
#print('\n')
print(json.dumps(jobs_json))

resp = requests.post('http://localhost:8000/susume/jobs/',json=jobs_json)
print(json.dumps(jobs_json))
print("RESPONSE: "+resp.text)
'''

# Just EN and ID
def update_simple(path,url,print_only=False):
    res = get_resource(path)
    simple_list = []

    # Scrub data here
    #
    #
        
    for k,v in res.items():
        simple_list.append(v)
    
    if print_only:
        pprint(simple_list)
        return

    resp = requests.post(url,json=simple_list)
    return resp

def update_jobs(path='jobs.lua',print_only=False):
    res = get_resource(path)
    jobs_list = []

    # Scrub data here
    #
    #

    for k,v in res.items():
        jobs_list.append(v)
    
    if print_only:
        pprint(jobs_list)
        return
    
    resp = requests.post('http://localhost:8000/susume/jobs/',json=jobs_list)


def update_spells(path='spells.lua',print_only=False):
    res = get_resource(path)
    spell_list = []

    for k,v in res.items():
        spell_list.append(v)
    
    for s in spell_list:
        # Scrub levels key
        if 'levels' in s: del s['levels']
        # Change range to spell_range
        s["spell_range"] = s.pop("range")
        # Change type to spell_type
        s["spell_type"] = s.pop("type")
        # Scrub overwrites key
        if 'overwrites' in s: del s['overwrites']
    if print_only:
        pprint(spell_list)
        return

    resp = requests.post('http://localhost:8000/susume/spells/',json=spell_list)
    return resp
    
    
######################################################
#   Update Spells
######################################################
'''
resp = update_spells(print_only=True)

spells_resp = update_spells()
print(resp.status_code)
'''
######################################################
#   Update Jobs
######################################################

#jobs_resp = update_jobs(print_only=True)
#jobs_resp = update_jobs()
#print(jobs_resp.status_code)

######################################################
#   Update Servers
######################################################

#server_resp = update_simple(path='servers.lua',url=local_url+'servers',print_only=True)
server_resp = update_simple(path='servers.lua',url=local_url+'servers')
print(server_resp.status_code)