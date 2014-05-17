from __future__ import print_function
from urllib2 import Request, urlopen, URLError
import urllib, base64, os, sys

#########################################################################
# TextEncode is a small tool in which you can encode and deocde text    #
# using fifteen selected ciphers. This is based on a online API.        #
#                                                                       #
# Copyright (C) 2014 Osanda Malith Jayathissa                           #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# any later version.                                                    #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#########################################################################

class TextEncode(object):
	def __init__(self, msg, option, key, cipher):
		self.msg = msg
		self.option = option
		self.key = key
		self.cipher = cipher
	
	def crypt(self):		
		option = {
				1	: 'encrypt',
				2   : 'decrypt'
			}
		option = str(option.get(self.option))
	
		cipher = {
				1	:	1,
				2   :	2,
				3   :	3,
				4   :	4,
				5   :	5,
				6   :	6,
				7   :	7,
				8   :	8,
				9   :	9,
				10  :	10,
				11	:	11,
				12	:	12,
				13	:	13,
				14	:	14,
				15	:	15
		}
		cipher = str(cipher.get(self.cipher))
		
		payload  = { 
			'request' : option,
			't' : cipher,
			'p' : self.key,
			's' : self.msg

		 }
		
		payload = urllib.urlencode(payload)
		rev = '\x3d\x3d\x77\x4c\x6c\x31\x57\x59\x75\x35\x69\x64\x79\x42\x33\x4c\x76\x6f\x44\x63\x30\x52\x48\x61'
		host = ''
		i = len(rev) -1
		while i >= 0:
			host += rev[i]
			i -= 1
		host = str(base64.decodestring(host))
		url = host + 'api.php?' + payload
		request = Request(url)
		try:
			response = urlopen(request)
			out = response.read()
			if option == 'encrypt':
				print ('[~] Encrypted text is: {0}'.format(str(out)))
			else:
				print ('[~] Decrypted text is: {0}'.format(str(out)))
		except URLError:
		    print ('[!] Are you connected to the Internet?')

def banner():
	banner = '''
\t _______        _   ______                     _      
\t|__   __|      | | |  ____|                   | |     
\t   | | _____  _| |_| |__   _ __   ___ ___   __| | ___ 
\t   | |/ _ \ \/ / __|  __| | '_ \ / __/ _ \ / _` |/ _ \\
\t   | |  __/>  <| |_| |____| | | | (_| (_) | (_| |  __/
\t   |_|\___/_/\_\\\\__|______|_| |_|\___\___/ \__,_|\___|
\n
\t\t[*] Author: Osanda Malith Jayathissa
\t\t[*] Follow @OsandaMalith
'''
	return banner

def cls():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def main():
	cls()
	print ('{0}'.format(banner()))
	try:
		msg = str(raw_input('[*] Enter your msg: '))
		while True:
			try:
				encdec = int(raw_input('1. Encode\n2. Decode \n'))
				break
			except ValueError:
				print ('[!] Enter only a number')
				continue
		key = str(raw_input('[*] Enter your key: '))
		print ('''\n[?] Choose a cipher\n
01. AES128
02. AES192
03. AES256  
04. BLOWFISH  
05. CAST128  
06. CAST256  
07. DES  
08. GOST  
09. LOKI97  
10. RC2  
11. SAFERPLUS  
12. SERPENT  
13. TRIPLEDES  
14. TWOFISH  
15. XTEA  

		''')
		while True:
			try:
				choice = int(raw_input(''))
				break
			except ValueError:
				print ('[!] Enter only a number')
				continue
		TextEncode(msg,encdec,key, choice).crypt()
	except KeyboardInterrupt:
			print ('[!] Ctrl + C detected\n[!] Exiting')
			sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)
	
if __name__ == "__main__": 
    main()  
#EOF