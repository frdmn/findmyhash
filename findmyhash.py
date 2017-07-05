# -*- coding: iso-8859-1 -*-

########################################################################################################
### LICENSE
########################################################################################################
#
# findmyhash.py - v 1.1.2
#
# This script is under GPL v3 License (http://www.gnu.org/licenses/gpl-3.0.html).
#
# Only this source code is under GPL v3 License. Web services used in this script are under
# different licenses. 
#
# If you know some clause in one of these web services which forbids to use it inside this script,
# please contact me to remove the web service as soon as possible.
#
# Developed by JulGor ( http://laxmarcaellugar.blogspot.com/ )
# Mail: bloglaxmarcaellugar AT gmail DOT com
# twitter: @laXmarcaellugar
#
#######################################################################################################

#######################################################################################################
### WHAT IS THE DIFFERENCE BETWEEN MY VERSION AND HIS
#######################################################################################################
#
# For now, it only accepts MD5 checksums, and the "google search" is no longer available, that is why
# I was preparing this tool to work along my other one called TextDump. As that was only necessary md5
# searching system and the google search wouldn't work well.
#
#######################################################################################################


#######################################################################################################
### POST SCRIPTUM
########################################################################################################
#
# This script found at Lord13's GitHub account is a modification of Find My Hash, my main tool can be
# found at the main brach. While this version is from "findmyhash-mod" brach.
#
# For that, I had searched for many DBs that are still online and then updated Find My Hash.
#
# If you are looking for the official relase of Find My Hash, have in mind that he hasn't released any
# new version since that days, the newest you can find is availableat the website describe at "LICENSE"
# section. Or at his GitHub account (https://github.com/frdmn/findmyhash).
#
#######################################################################################################


########################################################################################################
### IMPORTS
########################################################################################################

try:
	import sys
	import hashlib
	from random import randint
	from re import search, findall
	from base64 import b64encode
	from os import system, name
except ImportError:
	print """
Execution error:

  You required some basic Python libraries. 
  
  This application use: sys, hashlib, urllib, urllib2, os, re, random, getopt, base64 and cookielib.

  Please, check if you have all of them installed in your system.

"""
	exit(1)
try:
	from bs4 import BeautifulSoup
except ImportError:
	print """
Execution error:
	
	You require BeautifulSoup4 to work. Please install it before using this tool.
	"""
	sys.exit(1)
try:
	import requests
except ImportError:
	print """
Execution error:
	
	You require requests to work. Please install it before using this tool.
	"""
	sys.exit(1)

system("cls") if name == 'nt' else system("clear")

########################################################################################################
### CONSTANTS
########################################################################################################

MD5 	= "md5"
SHA1 	= "sha1"

USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 1.0.5)",
	"curl/7.7.2 (powerpc-apple-darwin6.0) libcurl 7.7.2 (OpenSSL 0.9.6b)",
	"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b8pre) Gecko/20101213 Firefox/4.0b8pre",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
	"Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
	"Opera/9.80 (X11; Linux i686; U; pl) Presto/2.6.30 Version/10.61",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/535.1",
	"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
	]
	


########################################################################################################
### CRACKERS DEFINITION
########################################################################################################

class GROMWEB: 
	
	name = 		"gromweb"
	url = 		"http://md5.gromweb.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "https://md5.gromweb.com/?md5=%s" % (hashvalue)
		
		# Make the request
		response = requests.get(url)
		
		# Analyze the response
		html = None
		if response:
			html = response.text
		else:
			return None

		soup = BeautifulSoup(html, 'html.parser')

		for i in soup.find_all('em'):
			if i['class'] == [u'long-content', u'string']: return i.text

class MY_ADDR:
	
	name = 		"my-addr"
	url = 		"http://md5.my-addr.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
		
		# Build the parameters
		params = { "md5" : hashvalue,
			   "x" : '21',
			   "y" : '8' }
		
		# Make the request
		response = requests.post(url, data=params)
		
		# Analyze the response
		html = None
		if response:
			html = response.text
		else:
			return None
		
		match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", html)
		
		if match:
			return match.group().split('span')[2][3:-6]
		else:
			return None

class MD5DECRYPTION:
	
	name = 		"md5decryption"
	url = 		"http://md5decryption.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = self.url
		
		# Build the parameters
		params = { "hash" : hashvalue,
			   "submit" : "Decrypt It!" }
		
		# Make the request
		response = requests.post(url, data=params)
		
		# Analyze the response
		html = None
		if response:
			html = response.text
		else:
			return None
		
		match = search (r"Decrypted Text: </b>[^<]*</font>", html)
		
		if match:
			return match.group().split('b>')[1][:-7]
		else:
			return None

class HASHCRACK:
	
	name = 		"hashcrack"
	url = 		"http://hashcrack.com"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://hashcrack.com/index.php"
		
		# Build the parameters
		params = { "auth" : "8272hgt",
			   "hash" : hashvalue,
			   "string" : "",
			   "Submit" : "Submit" }
		
		# Make the request
		response = requests.post( url, data=params )
		
		# Analyze the response
		html = None
		if response:
			html = response.text
		else:
			return None
		
		match = search (r'<div align=center>"[^"]*" resolves to</div><br><div align=center> <span class=hervorheb2>[^<]*</span></div></TD>', html)
		
		if match:
			return match.group().split('hervorheb2>')[1][:-18]
		else:
			return None

class REDNOIZE:
	
	name = 		"rednoize"
	url = 		"http://md5.rednoize.com"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		
		url = "http://hashtoolkit.com/reverse-hash/?hash=%s" % (hashvalue)
		
		# Make the request
		response = requests.get(url)
		
		# Analyze the response
		html = response.text
		soup = BeautifulSoup(html, 'html.parser')

		for i in soup.find_all('span'):
			if i.get("title") == 'decrypted md5 hash': return i.text
			
class CMD5:
	
	name = 		"cmd5"
	url = 		"http://www.cmd5.org"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Look for hidden parameters
		response = requests.get( "http://www.cmd5.org/" )
		
		html = response.text
		
		soup = BeautifulSoup(html, 'html.parser')

		for i in soup.find_all('input'):
			if i.get("name") == "__VIEWSTATE":
				viewstate = i.get("value")

			if i.get("name") == "__VIEWSTATEGENERATOR":
				viewstategenerator = i.get("value")
			
			if i.get("name") == "ctl00$ContentPlaceHolder1$HiddenField1":
				got = i.get("value")
				ContentPlaceHolder1 = i.get("value") if got != None else ''
			
			if i.get("name") == "ctl00$ContentPlaceHolder1$HiddenField2":
				ContentPlaceHolder2 = i.get("value")
		
		# Build the URL
		url = "http://www.cmd5.org/"
		
		hash2 = ""
		if alg == MD5:
			hash2 = hashvalue
		else:
			if ':' in hashvalue:
				hash2 = hashvalue.split(':')[1]

		
		# Build the parameters
		params = { "__EVENTTARGET" : "",
			   "__EVENTARGUMENT" : "",
			   "__VIEWSTATE" : viewstate,
			   "__VIEWSTATEGENERATOR": viewstategenerator,
			   "ctl00$ContentPlaceHolder1$TextBoxInput" : hashvalue,
			   "ctl00$ContentPlaceHolder1$InputHashType" : "md5(unicode)",
			   "ctl00$ContentPlaceHolder1$Button1" : "decrypt",
			   "ctl00$ContentPlaceHolder1$HiddenField1" : ContentPlaceHolder1,
			   "ctl00$ContentPlaceHolder1$HiddenField2" : ContentPlaceHolder2 }
			   
		header = { "Referer" : "http://www.cmd5.org/" }
		
		# Make the request
		response = requests.post( url, data=params, headers=header )
		
		# Analyze the response
		html = None
		if response:
			html = response.text
		else:
			return None
		

		soup = BeautifulSoup(html, 'html.parser')
		found = soup.find_all(lambda tag: tag.get('id') == 'ctl00_ContentPlaceHolder1_LabelAnswer')[0].get_text()[:-14]
		
		return found if found else None

class MD5DECRYPT:
	
	name = 		"sans"
	url = 		"http://isc.sans.edu"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://www.md5decrypt.org"
		
		# Build the Headers with a random User-Agent
		response = requests.get(url)

		if response:
			html = response.text
		else:
			return None

		soup = BeautifulSoup(html, 'html.parser')

		match = soup.find_all(lambda tag: 'var jscheck=' in tag.text)
		
		jscheck = str(match[-1]).split("'")[1]
		hashvalue = b64encode(hashvalue)
		
		params = { "jscheck" : jscheck,
			   "value" : hashvalue,
			   "operation" : "MD5D" }
		
		url = "http://www.md5decrypt.org/index/process"
		# Make the request
		response = requests.post(url, data=params)

		if response:
			return dict(response.json())['body']
		else:
			return None

class CLAVEY:
	
	name = 		"Clavey Contrasena"
	url = 		"http://descodificar.claveycontraseña.es"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "http://descodificar.claveycontraseña.es/%s.html" % (hashvalue)
		
		response = requests.get(url)
		html = response.text
		if "404 : PAGE NOT FOUND" in html: return None

		soup = BeautifulSoup(html, 'html.parser')
		divs = soup.find_all('div', {'class': 'ver'})
		divs = list(set(divs))
		
		return divs[0]['onclick'].split('\'')[1]

class MD5DECODER:
	
	name = 		"md5decoder"
	url = 		"http://md5decoder.org"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "https://crackhash.com/"

		params = {
			'hash': hashvalue,
			'crack': 'crack'
		}

		response = requests.post(url, data=params)
		html = response.text

		soup = BeautifulSoup(html, 'html.parser')

		return soup.find_all('center')[0].get_text().split()[-1]

class MD5DB:
	
	name = 		"md5db"
	url = 		"https://md5db.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		"""Return True if HASHCRACK can crack this type of algorithm and
		False if it cannot."""
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		"""Try to crack the hash.
		@param hashvalue Hash to crack.
		@param alg Algorithm to crack."""
		
		# Check if the cracker can crack this kind of algorithm
		if not self.isSupported (alg):
			return None
		
		# Build the URL
		url = "https://md5db.net/api/%s" % hashvalue

		response = requests.get(url)
		html = response.text

		return html

CRAKERS = [
		GROMWEB,
		MY_ADDR,
		MD5DECRYPTION,
		HASHCRACK,
		REDNOIZE,
		CMD5,
		MD5DECRYPT,
		CLAVEY,
		MD5DECODER,
		MD5DB]



########################################################################################################
### GENERAL METHODS
########################################################################################################
def printSyntax ():
	"""Print application syntax."""
	
	print """

findmyhash 1.1.2 ( http://code.google.com/p/findmyhash/ )
hashabitch   2.0 ( https://github.com/MasterTuto/Hash-a-Bitch/tree/findmyhash-mod )

Usage: 
------

  python %s <algorithm> OPTIONS


Accepted algorithms are:
------------------------

  MD5       - RFC 1321
  SHA1      - RFC 3174 (FIPS 180-3) (Not yet)
 


Valid OPTIONS are:
------------------

  -H <hash_value>  If you only want to crack one hash, specify its value with this option.


Example:
---------

  -> Try to crack only one hash.
     python %s MD5 -H 098f6bcd4621d373cade4e832627b4f6
     
     
Contact:
--------

La X Marca El Lugar:
[Web]           http://laxmarcaellugar.blogspot.com/
[Mail/Google+]  bloglaxmarcaellugar@gmail.com
[twitter]       @laXmarcaellugar


Lord13 [WHO UPDATED]:
[Web]			https://forum.fsocietybrasil.org/profile/8-lord13/
[Mail]			mastertutobrasil@gmail.com
""" % ( (sys.argv[0].split('\\')[-1],) * 2 )



def crackHash (algorithm, hashvalue=None, hashfile=None):
	"""Crack a hash or all the hashes of a file.
	
	@param alg Algorithm of the hash (MD5, SHA1...).
	@param hashvalue Hash value to be cracked.
	@param hashfile Path of the hash file.
	@return If the hash has been cracked or not."""
	
	global CRAKERS
	
	# Cracked hashes will be stored here
	crackedhashes = []
	
	# Is the hash cracked?
	cracked = False
	
	# Only one of the two possible inputs can be setted.
	if (not hashvalue and not hashfile) or (hashvalue and hashfile):
		return False
	
	hashestocrack = [hashvalue]
	
	
	# Try to crack all the hashes...
	for activehash in hashestocrack:
		hashresults = []
		
		# Standarize the hash
		activehash = activehash.strip()
		
		# Initial message
		print "\nCracking hash: %s\n" % (activehash)

		# Each loop starts for a different start point to try to avoid IP filtered
		begin = randint(0, len(CRAKERS)-1)
		
		for i in range(len(CRAKERS)):
			# Select the cracker
			cr = CRAKERS[ (i+begin)%len(CRAKERS) ]()
			
			# Check if the cracker support the algorithm
			if not cr.isSupported ( algorithm.lower() ):
				continue
			
			# Analyze the hash
			print "Analyzing with %s (%s)..." % (cr.name, cr.url)
			
			# Crack the hash
			result = None
			try:
				result = cr.crack ( activehash, MD5 )
			# If it was some trouble, exit
			except:
				continue
			
			cracked = 0
			if result:
				# If it is a hashlib supported algorithm...
				h = hashlib.new (algorithm)
				h.update (result)
				
				if h.hexdigest() == activehash:
					hashresults.append (result)
					cracked = 2
				else:
					print "\033[31mHASH NOT FOUND AT %s (%s)\n\033[0;0m" % (cr.name, cr.url)
			else:
					print "\033[31mHASH NOT FOUND AT %s (%s)\n\033[0;0m" % (cr.name, cr.url)
			# Had the hash cracked?
			if cracked:
				print "\033[32m\n***** HASH CRACKED!! *****\nThe original string is: \033[33m%s\n\033[0;0m" % (result)
				# If result was verified, break
				if cracked == 2:
					exit()
		
		
		
		print "\033[31m\n**** HASH NOT CRACKED!! *****\nThe hash you gave is: %s\n\033[0;0m" % (hashvalue.strip())
		exit(0)
		# Store the result/s for later...
		if hashresults:
			
			# With some hash types, it is possible to have more than one result,
			# Repited results are deleted and a single string is constructed.
			resultlist = []
			for r in hashresults:
				if r not in resultlist:
					resultlist.append (r)
					
			finalresult = ""
			if len(resultlist) > 1:
				finalresult = ', '.join (resultlist)
			else:
				finalresult = resultlist[0]
			
			# Valid results are stored
			crackedhashes.append ( (activehash, finalresult) )
	
	
	# Loop is finished. File can need to be closed
	if hashfile:
		try:
			hashestocrack.close ()
		except:
			pass
		
	# Show a resume of all the cracked hashes
	# print "\nThe following hashes were cracked:\n----------------------------------\n"
	# print crackedhashes and "\n".join ("%s -> %s" % (hashvalue, result.strip()) for hashvalue, result in crackedhashes) or "NO HASH WAS CRACKED."
	# print
	
	#return result



'''
def searchHash (hashvalue):
	#Google the hash value looking for any result which could give some clue...
	
	#@param hashvalue The hash is been looking for.
	
	start = 0
	finished = False
	results = []
	
	sys.stdout.write("\nThe hash wasn't found in any database. Maybe Google has any idea...\nLooking for results...")
	sys.stdout.flush()
	
	while not finished:
		
		sys.stdout.write('.')
		sys.stdout.flush()
	
		# Build the URL
		url = "http://www.google.com/search?hl=en&q=%s&filter=0" % (hashvalue)
		if start:
			url += "&start=%d" % (start)
			
		# Build the Headers with a random User-Agent
		headers = { "User-Agent" : USER_AGENTS[randint(0, len(USER_AGENTS))-1] }
		
		# Send the request
		response = requests.get(url, headers=headers)
		
		# Extract the results ...
		html = None
		if response:
			html = response.text
		else:
			continue
		
		soup = BeautifulSoup(html, 'html.parser')
		
		resultlist = []
		print soup.find_all('h3')[0].a['href']
		
		for i in soup.find_all('h3'):
			resultlist.append(i.a.get('href'))

		print resultlist
		
		# If there is no a new result, finish
		if not new:
			finished = True
		
	
	# Show the results
	if results:
		print "\n\nGoogle has some results. Maybe you would like to check them manually:\n"
		
		results.sort()
		for r in results:
			print "  *> %s" % (r)
		print
	
	else:
		print "\n\nGoogle doesn't have any result. Sorry!\n"
'''

########################################################################################################
### MAIN CODE
########################################################################################################

def main(algorithm, hashvalue, googlesearch=True):
	"""Main method."""
	
	cracked = 0
	
	
	###################################################
	# Crack the hash/es
	crackHash(algorithm, hashvalue)

	# if not cracked and googlesearch and not hashfile:
	# 	print searchHash (hashvalue)
	

arguments = sys.argv
if '-h' in arguments: printSyntax();exit(0)

try:
	if arguments[1] != "-H": algorithm = arguments[1]
	else: raise SyntaxError
	hashvalue = arguments[arguments.index('-H')+1]
except:
	print "SyntaxError: Try help to see details of usage:\n\tpython %s -h" % arguments[0].split('\\')[-1]
	exit(1)

main(algorithm, hashvalue)
