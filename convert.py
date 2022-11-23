#!/usr/bin/env python

import os
import sys
import argparse
import json
import yaml
import toml			#pip3 install toml
import re
import time
from tqdm import tqdm		#pip3 install tqdm 

my_parser = argparse.ArgumentParser(description='Data file format converter', usage='--out {json, toml, yaml} [--in {json,yaml,toml}] [--output-file OUTPUT_FILE] [--print-only] file')

my_parser.add_argument('--out', type=str, help='The output file format', required=True)
my_parser.add_argument('--inp', type=str, help="input file format") 
my_parser.add_argument('--output-file', '-o', type=str, help="the output filename")
my_parser.add_argument('--print-only','-p', action='store_true', help='Print converted file contents to console')
my_parser.add_argument('file', type=str, help='input file')

args = my_parser.parse_args()

output_filename = args.output_file
input_file = sys.argv.pop()		#Get the name of the input file

if (not(output_filename)):		#Use the default filename which is same as input file name
	match = re.search(r'\w+(?=\.)', input_file) 
	output_file = match.group() + '.' + args.out
	print ("Default filename was used: " , output_file)
else:
	output_file = args.output_file + '.' + args.out		#Use the given name for the output file
	with open (output_file, 'a'):
		print ("Filename has been changed: ", output_file)
	
input_file_type = input_file[-4:]	#Get the input file format
output_file_type = args.out

with open (input_file, 'r') as file: 		#Checking the input file format to load it properly
	if (input_file_type == 'yaml'):
		config = yaml.safe_load(file)
	elif (input_file_type == 'json'):
		config = json.load(file)
	elif (input_file_type == 'toml'):
		config = toml.load(file)
	else:
		print ("Wrong file type, Please enter a correct one that ends with .{json, yaml or toml}")
		exit 
		
with open (output_file, 'w') as output:		#Checking the output file format to convert it properly
	if (output_file_type == 'yaml'):
		yaml.dump(config, output)
	elif (output_file_type == 'json'):
		json.dump(config, output)
	elif (output_file_type == 'toml'):
		toml.dump(config, output)
	else:
		print ("Wrong file type, Please enter a correct one that ends with .{json, yaml or toml}")
		exit 
		
if (args.print_only == True):			#Print the content of the file ONLY on the console OR create a new file with the given output format
	for i in tqdm (range (100), desc = "Converting..."):
		time.sleep(0.01)
	print ("The file's format has been converted successfully ")
	print ("The modified file's content can be shown below:\n")
	if (output_file_type == 'json'):
		outp = json.dumps(json.load(open(output_file)), indent = 2)
		print (outp)
	else:
		with open (output_file, 'r') as output:
			print (output.read())
else:
	for i in tqdm (range (100), desc = "Converting..."):
		time.sleep(0.01)
	print ("The file's format has been converted successfully ")
	print ("The modified file has been created successfully -->", output_file)
