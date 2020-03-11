import java.io.*;
import java.util.*;
class Alr
{

public static void main(String args[]){
char[] a=new char[7];

Console c = System.console();
String exp=c.readLine("Enter Your exp ");
for(int i=0;i<exp.length();i++)
a[i]=exp.charAt(i);
int ch=Integer.parseInt(c.readLine("Enter Your Choice: 1.Create ST \t 2.Search Symbol 3.Remove Symbol"));
Random rand = new Random();
char[] chars = exp.toCharArray();
int length=chars.length;
switch(ch){
case 1:
System.out.println("Symbol \t Address \t Type" );
	for(int i=0;i<length;i++)
	{
	if((chars[i] >='a' && chars[i]<='z') || (chars[i]>='A' && chars[i]<='Z'))
		System.out.println(chars[i] +"|  " + rand.nextInt(900000) + 10000 + " | IDENTIFIER");
		
	else 
		System.out.println(chars[i] + "|  " +rand.nextInt(900000) + 10000 +" | OPERATOR");
	}

for(char ab:a)
System.out.print(ab);
break;

case 2:
	String s=c.readLine("Enter symbol:");
	char cc =s.charAt(0); 
	for(char aa:a){
		if(aa == cc)
		{
			if(aa== '=' || aa=='+')
			System.out.println(aa +"|  " + rand.nextInt(900000) + 10000 + " | OPERATOR");
		
			else 
			System.out.println(aa + "|  " +rand.nextInt(900000) + 10000 +" | IDENTIFIER");
		}
		 
		}
		break;
}			
	
}
}
