/**Compare the substring of a string using Lexicographical order*/

import java.util.Scanner;

public class SubstringComparison {
		
	public static String getSmallestAndLargest(String s, int k) {
		String smallest = "";
        String largest = "";
        
        int size = s.length()-(k-1);
        String[] subStr = new String[size];
        
        for(int i=0; i<size; i++) {
        	subStr[i] = s.substring(i, i+k);
        }
        
        smallest = subStr[0];
        for(int i=0; i<subStr.length;i++) {
        	String each = subStr[i];
        	if(each.compareTo(smallest) < 0) {
        		System.out.println("rslt:"+each.compareTo(smallest));
        		smallest = each;       		
        		//System.out.println("s:" +smallest);
        	}
        	else if(each.compareTo(largest) > 0) {
        		largest = each;
        		//System.out.println("l:" + largest);
        	}
        }
        
        return smallest + "\n" + largest;
	}
	
	
	
	public static void main(String[]args) {
		Scanner in = new Scanner(System.in);
		/*First input is a string for comparison*/
		String s = in.next();
		/*Second input is the length of substrings to find*/
		int k = in.nextInt();
		in.close();
		
		System.out.println(getSmallestAndLargest(s,k));		
	}
}
