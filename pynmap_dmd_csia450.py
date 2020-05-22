#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "David Martinez"
__email__ = "davidmartinez8925@gmail.com"
__date_ = "Spring 2020"
__version__ = "0.0.1"

# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess
 
os.chdir('C:\\Users\\david')

cwd = os.getcwd()
print(cwd)

# SET VARIABLES
my_dir = 'C:\\Users\\david\\LoginID'
date_str = date.today().strftime("%m%d%y")
my_pickle = 'C:\\Users\\david\\LoginID\\%s.pickle' % date_str
my_json = 'C:\\Users\\david\\LoginID\\%s.json' % date_str
port_list = ['192.168.1.1:80', '192.168.1.1:23', '192.168.1.1:22']
nmap_path = 'C:\\Program Files (x86)\\Nmap\\nmap.exe'
nmap_network = '192.168.1.1/24'


def create_directory():   
    if(os.path.isdir(my_dir)) == False:
        try:  
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir) 
        except OSError:  
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir) 
        
        
def create_date_string():
    my_pickle= date.today().strftime('%m%d%y.pickle')
    my_json = date.today().strftime('%m%d%y.json')
   # print ('Date String:', date_str)
    return my_pickle, my_json

def write_files(my_pickle,my_json, nmap_data):

    # write the pickle file

    with open(my_pickle, 'wb') as fp:
        pickle.dump(nmap_data, fp)
    fp.close()

#    json_nmap = json.dumps(nmap_data)
    # write the json file

#    with open(my_json, 'w') as fp:
 #      json.dump(nmap_data, fp)
  #  fp.close()


def read_files(my_pickle, my_json):
    

    # read the pickle file

    with open(my_pickle, 'rb') as fp:
        infile = pickle.load(fp)
    fp.close()

    print ('pickle:', infile)
    

    # read the json file

#    with open(my_json, 'r') as fp:
#        port_list = json.load(fp)
#    fp.close()

 #   print ('json:', port_list)


def run_nmap():
    nmap_out = subprocess.run([nmap_path, '-T4', nmap_network],
                              capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    return nmap_data


nmap_data = run_nmap()
my_pickle, my_json = create_date_string()
write_files(my_pickle,my_json, nmap_data)
read_files(my_pickle, my_json)

