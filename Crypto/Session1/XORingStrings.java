import java.util.*;
class XORingStrings{
	public static void main(String args[]){
		Scanner s= new Scanner(System.in);
		String a="1c0111001f010100061a024b53535009181c";
		String b="686974207468652062756c6c277320657965";
		String x="";
		for(int i=0;i<a.length();i++){
			x=x+toHex(fromHex(a.charAt(i))^fromHex(b.charAt(i)));
		}
		System.out.println(x);
	}
	static int fromHex(char a){
		int x=0;
		if(a>='0'&&a<='9'){
			x=a-'0';
		}
		if(a>='a'&&a<='f'){
			x=a-'a'+10;
		}
		if(a>='A'&&a<='F'){
			x=a-'A'+10;
		}
		return x;
	}
	static char toHex(int n){
		String a="0123456789ABCDEF";
		return a.charAt(n);
	}
}	