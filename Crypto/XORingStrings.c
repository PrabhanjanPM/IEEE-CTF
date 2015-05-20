#include <stdio.h>
#include <string.h>
int main(){
        char a[100];
        char b[100];
        int i;
        for(i=0;i<100;i++){
                b[i]=i+35;
        }
        printf("Enter Plaintext- ");
        gets(a);
        for(i=0;i<strlen(a);i++){
                a[i]=a[i]^b[i];
        }
        printf("%s\n",a);
        return 0;
}