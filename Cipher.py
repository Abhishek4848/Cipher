#This function is defined to encode the given message.

def encode():

	a = input('Enter message to be encoded: ')
	b = a.strip()
	l = list(b)
	q = False
	while q == False:
		try:
			print("."*65)
			shift = int(input('Enter shift value: '))
			q = True
		except ValueError:
			continue
	en = list(map(lambda x:chr(ord(x) + shift), l))
	print("."*65)
	print ("Encoded message: ",''.join(en))
	print('.'*65) 
	
	
#This function is defined to decode the given message.

def decode():

	a = input('Enter message to be decoded: ')
	b = a.strip()
	l = list(b)
	q = False
	while q == False:
		try:
			print("."*65)
			shift = int(input('Enter shift value: '))
			q = True
		except ValueError:
			continue
	de = list(map(lambda x:chr(ord(x) - shift), l))
	print("."*65)
	print ("Decoded message: ",''.join(de))
	print('.'*65)
	
	
print('  1.) Encode\n  2.) Decode')
print('.'*65)
ch = ''
q = False
while (q != True):
	try:
		ch = int(input('Enter Your Choice: '))
		if ch == 1 or ch == 2:
			q = True
		else:
			q = False
	except ValueError:
		continue
if (ch == 1):
	print('Your message will be Encoded')
	print('.'*65)
	encode()
elif (ch == 2):
	print('Your message will be Decoded')
	print('.'*65)
	decode()
