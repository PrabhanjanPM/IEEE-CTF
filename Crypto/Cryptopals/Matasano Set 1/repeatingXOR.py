plaintext_1="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key="ICE"
ciphertext_1=""
ciphertext_2=""
j=0
for i in plaintext_1:
	ciphertext_1=ciphertext_1+chr(ord(key[j%3])^ord(i))
	j=j+1
print ciphertext_1.encode("hex")