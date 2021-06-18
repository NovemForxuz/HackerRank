import java.util.Scanner;
import java.util.ArrayList;

public class Anagrams {

	static boolean isAnagram(String a, String b) {
		// Complete the function
		boolean result = false;
		ArrayList<String> aStr = new ArrayList<String>();
		
		for(char ltr: a.toCharArray()) {
			aStr.add(String.valueOf(ltr)); 		//populate the array with elements of a
		}
		logArr(aStr);		//log
		
		for (int i = 0; i < b.length(); i++) {
			String letter = String.valueOf(b.charAt(i));
			if(aStr.contains(letter)){
				int index = aStr.indexOf(letter);
				aStr.remove(index);
				logArr(aStr);
			}
			
		}
		if(aStr.isEmpty() && a.length()==b.length()) {
			result = true;
		}
		return result;
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String a = scan.next();
		String b = scan.next();
		scan.close();
		boolean ret = isAnagram(a, b);
		System.out.println((ret) ? "Anagrams" : "Not Anagrams");
	}
	
	public static void logArr(ArrayList<String> arr2BLog) {
		System.out.print("[");
		for(String s:arr2BLog) {
			System.out.print(" " + s);
		}
		System.out.println(" ]");
	}
}