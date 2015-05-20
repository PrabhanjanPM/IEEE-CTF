#include <stdio.h>
#include <string.h>
int main(){
        char a[100];
        char b[100];
        int i;
        printf("Enter Plaintext- ");
        gets(a);
        printf("Enter key(same length as the plaintext)- ");
        gets(b);
        for(i=0;i<strlen(a);i++){
                a[i]=a[i]^b[i];
        }
        printf("Ciphertext- %s\n",a);
        return 0;
}