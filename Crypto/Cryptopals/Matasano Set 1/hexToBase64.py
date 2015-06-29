hex="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hexDict={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
"a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
#replace dictionary with list
i=0
list=[]
list1=[]
while i<len(hex):
	list.append(hexDict[hex[i]]+hexDict[hex[i+1]]+hexDict[hex[i+2]])
	i=i+3;
for i in range(0,len(list)):
	first=list[i][:6]
	list1.append(int(first[:1])*32+int(first[1:2])*16+int(first[2:3])*8+int(first[3:4])*4+int(first[4:5])*2+int(first[5:6])*1)
	second=list[i][6:12]
	list1.append(int(second[:1])*32+int(second[1:2])*16+int(second[2:3])*8+int(second[3:4])*4+int(second[4:5])*2+int(second[5:6])*1)
list64=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0',
'1','2','3','4','5','6','7','8','9','+','/']
str=""
for i in list1:
	str=str+list64[i]
print str