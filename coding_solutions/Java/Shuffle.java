package ques6;

import java.util.*;
public class Shuffle {

	// str1="abc" and str2="def", str3="dabecf"
	
	public boolean isShuffle(String st1,String st2,String st3) {
		
		int cs1=0,cs2=0;
		boolean isShuffled=false;
		char[] str1 = st1.toCharArray();
		char[] str2 = st2.toCharArray();
		char[] str3 = st3.toCharArray();
		for(int i=0 ; i<str3.length;i++) {
			
	
				if(cs1<=str1.length-1 && str3[i]==str1[cs1]) {
					cs1++;
					isShuffled=true;
				}
				else if (cs2<=str2.length-1 && str3[i]==str2[cs2]) {
					cs2++;
					isShuffled=true;
				}
				else {
					return false;
				}
		
		}
		
		return isShuffled;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc  = new Scanner(System.in);
		String str1= sc.next();
		String str2 = sc.next();
		String str3 = sc.next();
		Shuffle sh = new Shuffle();
		if(sh.isShuffle(str1,str2,str3)) {
			System.out.println("Shuffle");
		}
		else {
			System.out.println("Not a Shuffle");
		}
		sc.close();
	}
	
	

}
