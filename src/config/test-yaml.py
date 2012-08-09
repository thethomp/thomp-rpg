#!/usr/bin/python
import yaml

yamlfile = open('dialog.yaml', 'r')

for data in yaml.load_all(yamlfile):
	print data
	#print data['name']
	#print data['description']
