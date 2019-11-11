#This function is defined to encode the given message.
def encode():
	a=input('Enter message to be encoded:')
	b=a.strip()
	l=list(b)
	shift=int(input('Enter shift value :'))
	en=list(map(lambda x:chr(ord(x)+shift),l))
	s=''
	print (''.join(en))
	print('.'*65) 
	
	
#This function is defined to decode the given message.
def decode():
	a=input('enter message to be decoded:')
	b=a.strip()
	l=list(b)
	shift=int(input('Enter shift value :'))
	de=list(map(lambda x:chr(ord(x)-shift),l))
	s=''
	print (''.join(de))
	print('.'*65)
	
	
print('1.) Encode \n 2.) Decode')
print('.'*65)
q = False
while (q!=True):
	ch=int(input('Enter Your Choice:'))
	if (ch==1):
		print('Your message will be Encoded')
		print('.'*65)
		encode()
	elif (ch==2):
		print('Your message will be Decoded')
		print('.'*65)
		decode()
	if (ch==1 or ch==2):
			q = True	
