def frequency(freq):
	for i in freq:
		e=0.0
		a=0.0
		o=0.0
		for j in i:
			if(j=='e'):
				e=e+1
			if(j=='a'):
				a=a+1
			if(j=='o'):
				o=o+1
		e=(e/len(i))*100
		a=(a/len(i))*100
		o=(o/len(i))*100
		if(e>=7 or a>=5 or o>=6):
			print "%f %f %f"%(a,e,o)
			print i
			print freq.index(i)	
hexString="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ascii=''.join(chr(int(hexString[i:i+2], 16)) for i in range(0, len(hexString), 2))
freq=[]
for j in range(0,256):
	xor=""	
	for i in ascii:
		xor=xor+chr(j^ord(i))
	freq.append(xor)
frequency(freq)