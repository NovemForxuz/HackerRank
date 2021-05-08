/**Given string A, print Yes if it a palindrome, print No letters*/
import java.util.Scanner;

public class StringReverse {
	public static void main(String[]args) {
		Scanner in = new Scanner(System.in);
		String A = in.next();
		String result = "";
		
		if(A.length()>1) {
			for(int i=0;i<A.length()/2;i++) {
				int j = A.length()-i-1;
				if(A.charAt(i) == A.charAt(j)) {
					result = "Yes";
				}else {
					result = "No";
				}
			}
		}else {
			result = "Yes";
		}
		
		System.out.println(result);
	}
}
