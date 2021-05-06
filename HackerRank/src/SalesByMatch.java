import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'sockMerchant' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY ar
     */

    public static int sockMerchant(int n, List<Integer> ar) {
    	// Write your code here
    	//hashmap<Key,Value> pair
        HashMap<Integer, Integer> color = new HashMap<Integer, Integer>();
        int sockPair = 0;
        
        //iterate through list
        for(int sock: ar){
            if(!color.containsKey(sock)){
            	//add into hashmap (key,value) if doesn't exist
                color.put(sock,1);
            }else{
            	//update value for key 'sock' in hasmap if exist
                color.put(sock, color.get(sock)+1);
            }
        }
        
        //iterate through hashmap
        Iterator it = color.entrySet().iterator();
        while(it.hasNext()) {
        	HashMap.Entry pair = (HashMap.Entry)it.next();
        	//update total number of pair for each color of sock 
        	sockPair += ((int)pair.getValue()/2);
        	//System.out.println("Pair of socks: " + sockPair);
        	it.remove();
        }
        
        return sockPair;
    }

}

public class SalesByMatch {
    public static void main(String[] args) throws IOException {
    	//Reading input
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        //Writing output
        /*BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));*/

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> ar = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.sockMerchant(n, ar);

        /*
         * bufferedWriter.write(String.valueOf(result));
         * bufferedWriter.newLine();
         */   
        System.out.println(result+"");

        bufferedReader.close();
        /*bufferedWriter.close();*/
    }
}
