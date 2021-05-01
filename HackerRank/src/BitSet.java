import java.io.*;
import java.util.*;
import java.math.*;
import java.text.*;
import java.util.regex.*;

public class BitSet {
	private static int n, m;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = Integer.parseInt(sc.next());
		m = Integer.parseInt(sc.next());

		java.util.BitSet b1 = new java.util.BitSet(n);
		java.util.BitSet b2 = new java.util.BitSet(n);
		java.util.BitSet[] bitset = new java.util.BitSet[3];
		
		bitset[1] = b1;
		bitset[2] = b2;

		while (0 < m--) {
			String operand = sc.next();
			int in1 = sc.nextInt();
			int in2 = sc.nextInt();

			switch (operand) {
			case "AND": {
				bitset[in1].and(bitset[in2]);
				break;
			}
			case "OR": {
				bitset[in1].or(bitset[in2]);
				break;
			}
			case "XOR": {
				bitset[in1].xor(bitset[in2]);
				break;
			}
			case "FLIP": {
				bitset[in1].flip(in2);
				break;
			}
			case "SET": {
				bitset[in1].set(in2);
				break;
			}
			}

			System.out.printf("%d %d%n", bitset[1].cardinality(), bitset[2].cardinality());

		}
	}
}
