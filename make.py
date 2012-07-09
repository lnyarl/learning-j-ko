#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib
import cgi
import os
import re
import sys
from HTMLParser import HTMLParser
print(sys.argv[1])
if len(sys.argv) != 2:
	print("첫 번째 인자로 변환할 url이 필요합니다.")
	sys.exit()

f = urllib.urlopen(sys.argv[1])
s = f.read()
s_line = s.split('\r\n')
#s = '<?xml version="1.0" encoding="UTF-8" ?>' + f.read()[63:]
f.close()

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	isstart = False
	tag = []
	f = None
	file_name = ""
	table_index = -1 
	tt_index = None

	pre_index = -1

	def end_parsing(self):
		if self.f != None:
			self.f.close()
			self.f = open(self.file_name, "r")
			s = self.f.read();
			s = re.sub(r'\r\n(\r\n)+', '\r\n\r\n', s)
			print(s)
			self.f.close()
			self.f = open(self.file_name, "w")
			self.f.write(s)
			self.f.close()


	def handle_starttag(self, tag, attrs):
		if tag.lower() == 'tr': self.isstart = True
		if tag.lower() == 'hr': 
			self.isstart = False
			self.end_parsing()
		if self.isstart == False: return

		self.tag.append(tag.lower())


		result = ""
		mode = tag.lower()

		if mode == 'p':
			result = "\r\n\r\n"
		elif mode == 'table':
			self.table_index = self.getpos()[0]-1
		elif mode == 'pre':
			self.pre_index = self.getpos()[0]
		elif mode == 'tt' and self.table_index < 0:
			self.tt_index = self.getpos()

		if self.f != None:
			self.f.write(result)


	def handle_endtag(self, tag):
		if self.isstart == False: return

		result = ""
		mode = tag.lower()

		if mode == 'table':
			result = " " + "\r\n".join(s_line[self.table_index:self.getpos()[0]])
			self.table_index = -1
		elif mode == 'pre':
			result = "\r\n\r\n\t" + "\r\n\t".join(s_line[self.pre_index:self.getpos()[0]-1]) + "\r\n\r\n"
			self.pre_index = -1
		elif mode == 'tt' and self.table_index < 0 and self.tt_index != None:
			result = '`' +s_line[self.tt_index[0]-1][self.tt_index[1]+4:self.getpos()[1]] +  '`'
			self.tt_index = None

		if self.f != None:
			self.f.write(result)

		self.tag.pop()

	def handle_data(self, data):
		if self.isstart == False or len(self.tag) == 0 or data.strip() == "": return
		mode = self.tag[len(self.tag) - 1]
		result = ''
		if mode == 'h1': 
			file_name = data[:data.index(':')].lower().replace(' ', '') + '.md'
			self.f = open(file_name, 'w')
			self.file_name = file_name

			result = self.getH1(data, mode)
		elif mode == 'h2' :
			result = self.getH2(data, mode)
		elif mode == 'h3' :
			result = self.getH3(data, mode)
		elif mode == 'h4' :
			result = self.getH4(data, mode)
		elif mode == 'table':
			result = self.getTable(data, mode)
		elif mode == 'tt' or mode == 'pre' :
			#result = self.getCode(data, mode)
			pass
		elif mode == 'p' :
			result = self.getP(data, mode)
		elif mode == 'br' :
			pass
		else:
			result = data.replace('\r\n', '')

		if result != None and self.f != None:
			self.f.write(result)
	
	def getH1(self, data, mode):
		return '# ' + data + '\r\n\r\n'
	
	def getH2(self, data, mode):
		return '\r\n\r\n## ' + data + '\r\n\r\n'

	def getH3(self, data, mode):
		return '\r\n\r\n### ' + data + '\r\n\r\n'

	def getH4(self, data, mode):
		return '\r\n\r\n### ' + data + '\r\n\r\n'

	def getTable(self, data, mode):
		return data

	def getCode(self, data, mode):
		if mode == 'pre' : # block code
			print(data)
			return '\r\n\t' + ('\r\n\t'.join(data.split('\r\n'))) + '\r\n'
	
	def getP(self, data, mode):
		return data.replace('\r\n', '') + ' '

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(s)
