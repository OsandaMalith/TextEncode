from __future__ import print_function
from urllib2 import Request, urlopen, URLError




class TextEncoder(object):
	def __init__(self, msg, option, key):
		self.msg = msg
		self.option = option
		self.key = key

	def choice(slef):
		AES128 - 1
		AES192 - 2
		AES256 - 3
		BLOWFISH - 4
		CAST128 - 5
		CAST256 - 6
		DES - 7
		GOST - 8
		LOKI97 - 9
		RC2 - 10
		SAFERPLUS - 11
		SERPENT - 12
		TRIPLEDES - 13
		TWOFISH - 14
		XTEA - 15

	def lol(self):
		request = Request('http://prv.name/api.php?request=encrypt&t=1&p=My%20Password&s=Lorem%20Ipsum')

		try:
			response = urlopen(request)
			kittens = response.read()
			print 'kittens'
		except URLError, e:
		    print 'No kittez. Got an error code:', e		


def banner():
	banner = '''
 
[*] Author: Osanda Malith Jayathissa 
[*] Follow @OsandaMalith
[*] Description: A Cross-Platform Forensic Framework for Google Chrome
'''
	return banner

def cls():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

def main():
	cls()
	print banner()
	try:
		while True:
			try:
				msg = string(input("[?] Enter your Message: " ))
			except Exception, e:
				print e
				continue
		while True:
			try:
				option = int(input("1. Encrypt\n2.Decrypt"))
			except Exception, e:
				print e
				continue
			if choice == 1:
				history = chromeFreak(PathName).HistoryObj()
				Start(history)
				break
			if choice == 2:
				downloads = chromeFreak(PathName).DownloadsObj()
				Start(downloads)
				break
			
			else:
				print '[!] Invalid Choice'

	except KeyboardInterrupt:
		print '[!] Ctrl + C detected\n[!] Exiting'
		sys.exit(0)
	except EOFError:
		print '[!] Ctrl + D detected\n[!] Exiting'
		sys.exit(0)
	

if __name__ == "__main__": 
    main()  