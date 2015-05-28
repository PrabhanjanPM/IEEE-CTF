import java.util.*;
public class VigenereCipherEncrypt{
	public static void main(String args[]){
		Scanner s= new Scanner(System.in);	
		String a= s.nextLine();
		a.toUpperCase();
		String b= s.nextLine();
		b.toUpperCase();
		String x="";
		for(int i=0;i<a.length();i++){
			x=x+(char)(((a.charAt(i)-'A')+(b.charAt(i%b.length())-'A'))%26+'A');
		}
		System.out.println(x);
	}
}