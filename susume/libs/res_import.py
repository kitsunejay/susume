#!python
import os
import sys
import platform
from slpp import slpp as lua
import json
from pprint import pprint
import requests
import re
import io

######################################

local_url = 'http://localhost:8000/susume/'

######################################



def get_resource(path,decode=True):
    if platform.system() == 'Windows':
        path = 'C:\\Program Files (x86)\\Windower4\\res\\' + path
    with open(path, encoding="utf8",newline='') as fd:
        data = fd.read().replace('return', '', 1)
        if decode: 
            return lua.decode(data)
        else:
            return data

def chunks(lst, n):
    """Yield successive n-sized chunks from lst"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def get_nonutf_resource(path):
    if platform.system() == 'Windows':
        path = 'C:\\Program Files (x86)\\Windower4\\res\\' + path
    with open(path, encoding="utf8",newline='') as fd:
        luastring = ""
        data = fd.read()
        #print(len(data))
        '''
        for i in range(len(data)):
            thisline = data[i]
            thisline = thisline.replace('return','',1)
            #thisline = re.sub(r"(\w)-(\w)",r"\1 \2",thisline)
            if re.match(".*\w-\w.*",data[i]):
                print(data[i])
                data[i].replace("-"," ", 1)
                print(data[i])

            #print(luastring,end = "\r\n")
        '''
        print(data)
        '''
            luastring = luastring + thisline
            
            for m in re.finditer('(?P<tag>\w+)=',luastring):
                print(m.group('tag'))
            '''
            # FIX ME # 
            #return lua.decode(luastring)
#get_nonutf_resource('item_descriptions.lua')


def lua_parse(string=''):
    return_dict = {}

    p = re.compile('\s*?\{{0,1}\s*?\[(?P<key>\d+)\]\s*?=\s*?{id=(?P<id>\d+),en=\"(?P<en>.+?)\",ja\=\"(?P<ja>.+)\"},{0,1}\}{0,1}',re.DOTALL)
    split_string = string.split('\r\n')

    for i in range(len(split_string)):
        try:
            key = p.match(split_string[i]).groupdict('key')
            this_dict = p.match(split_string[i]).groupdict()
            key = this_dict['key']
            del this_dict['key']
            return_dict[key] = this_dict
        except Exception as e:
            #print("ERROR: ["+str(i)+"] = "+ str(e))
            #print('['+split_string[i]+']')
            next
    return return_dict


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
    this_list = []

    # Scrub data here
    #
    #

    for k,v in res.items():
        this_list.append(v)
    
    if print_only:
        pprint(this_list)
        return
    
    resp = requests.post('http://localhost:8000/susume/jobs/',json=this_list)


def update_spells(path='spells.lua',print_only=False):
    res = get_resource(path)
    this_list = []

    for k,v in res.items():
        spell_list.append(v)
    
    for item in this_list:
        # Scrub levels key
        if 'levels' in item: del item['levels']
        # Change range to spell_range
        item["spell_range"] = item.pop("range")
        # Change type to spell_type
        item["spell_type"] = item.pop("type")
        # Scrub overwrites key
        if 'overwrites' in item: del item['overwrites']
    if print_only:
        pprint(this_list)
        return

    resp = requests.post(url,json=this_list)
    return resp
    
def update_abilities(url,path='job_abilties.lua',print_only=False):
    res = get_resource(path)
    this_list = []

    for k,v in res.items():
        this_list.append(v)
    
    for item in this_list:
        # Scrub levels key
        if 'levels' in item: del item['levels']
        # Change range to ability_range
        item["ability_range"] = item.pop("range")
        # Change type to ability_type
        item["ability_type"] = item.pop("type")

    if print_only:
        pprint(this_list)
        return

    resp = requests.post(url,json=this_list)
    return resp    

def update_equipment(url,path='items.lua',print_only=False):
    res = get_resource(path)
    res_desc = lua_parse(get_resource('item_descriptions.lua',decode=False))
    this_list = []

    for k in list(res.keys()):
        #print(res[k].keys())
        if res[k]["category"] != "Armor" and res[k]["category"] != "Weapon":
            #print(res[k])
            del res[k]
    
    # Add in item descriptions
    for k in res_desc.keys():
        if int(k) in res:
            try:
                res[int(k)]['desc_en'] = res_desc[k]['en']
            except Exception as e:
                print("en error: " + str(e))
            try:
                res[int(k)]['desc_ja'] = res_desc[k]['ja']
            except Exception as e:
                print("ja error: " + str(e))
    if print_only:
        print(len(res))
        pprint(res)
        return

    for k,v in res.items():
        this_list.append(v)
    for item in this_list:
        # Change type to ability_type
        item["equipment_type"] = item.pop("type")

    # Post in chunks
    chnk = []
    resp = []
    for c in chunks(this_list,1000):
        chnk.append(c)
    print(len(chnk))
    for c in chnk:
        resp.append(requests.post(url,json=c))
        
    return resp
######################################################
#   Update Spells
######################################################

#spells_resp = update_spells(path='spells.lua',url=local_url+'spells',print_only=True)
#spells_resp = update_spells(path='spells.lua',url=local_url+'spells')
#print(spells_resp.status_code)

######################################################
#   Update Jobs
######################################################

#jobs_resp = update_simple(path='jobs.lua',url=local_url+'jobs',print_only=True)
#jobs_resp = update_simple(path='jobs.lua',url=local_url+'jobs')
#print(jobs_resp.status_code)

######################################################
#   Update Servers
######################################################

#server_resp = update_simple(path='servers.lua',url=local_url+'servers',print_only=True)
#server_resp = update_simple(path='servers.lua',url=local_url+'servers')
#print(server_resp.status_code)

######################################################
#   Update Slots
######################################################

#slots_resp = update_simple(path='slots.lua',url=local_url+'slots',print_only=True)
#slots_resp = update_simple(path='slots.lua',url=local_url+'slots')
#print(slots_resp.status_code)

######################################################
#   Update Abiltiies
######################################################

#abilities_resp = update_abilities(path='job_abilities.lua',url=local_url+'abilities',print_only=True)
#abilities_resp = update_abilities(path='job_abilities.lua',url=local_url+'abilities')
#print(abilities_resp.status_code)

######################################################
#   Update Equipment (From Items.lua)
######################################################

#items_resp = update_equipment(path='items.lua',url=local_url+'equipment',print_only=True)
items_resp = update_equipment(path='items.lua',url=local_url+'equipment')
for r in items_resp:
    print(r.status_code)