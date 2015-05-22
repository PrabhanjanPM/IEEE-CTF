#include <stdio.h>
#include <string.h>
int main(){
        int fromHex(char);
        char toHex(int);
        char a[100];
        char b[100];
        int i;
        printf("Enter Plaintext- ");
        gets(a);
        printf("Enter key(same length as the plaintext)- ");
        gets(b);
        for(i=0;i<strlen(a);i++){
                a[i]=toHex(fromHex(a[i])^fromHex(b[i]));
        }
        printf("Ciphertext- %s\n",a);
        return 0;
}
int fromHex(char c){
	if(c>='0'&&c<='9'){
		c=c-'0';
	}
	if(c>='A'&&c<='F'){
		c=c-'A'+10;
	}
	if(c>='a'&&c<='f'){
		c=c-'a'+10;
	}
}
char toHex(int n){
	char *a="0123456789ABCDEF";
	return a[n];
}
       