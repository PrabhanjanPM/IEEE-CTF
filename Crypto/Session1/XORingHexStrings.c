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
        char x[strlen(a)+1];
        for(i=0;i<strlen(a);i++){
                x[i]=toHex(fromHex(a[i])^fromHex(b[i]));
        }
        x{strlen(a)+1]='\0';
        printf("Ciphertext- %s\n",x);
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
	char a[16]="0123456789ABCDEF";
	return a[n];
}
       