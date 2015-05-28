import java.util.*;
public class VigenereCipherDecrypt{
	public static void main(String args[]){
		Scanner s= new Scanner(System.in);	
		String a= s.nextLine();
		a.toUpperCase();
		String b= s.nextLine();
		b.toUpperCase();
		String x="";
		for(int i=0;i<a.length();i++){
			int k=(a.charAt(i)-'A')-(b.charAt(i%b.length())-'A');
			if(k<0)
				k=k+26;
			x=x+(char)((k)%26+'A');
		}
		System.out.println(x);
	}
}