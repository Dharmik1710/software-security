import hashlib
import string
import random

target = 'cb1bbe'
while True:
	# generating random strings with uppercase of length 6
	plaintext = ''.join(random.choices(string.ascii_uppercase, k=6))
    	
	# Generating hash
	hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()
    	if hash[:6] == target:
        	print('plaintext:"' + plaintext + '", md5:' + hash)
        	break
