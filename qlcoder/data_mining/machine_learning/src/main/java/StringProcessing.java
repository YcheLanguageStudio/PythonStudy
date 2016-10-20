import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

/**
 * Created by cheyulin on 10/20/16.
 */
public class StringProcessing {

    public static int differ(String left, String right) {
        int sameCount = 0;
        for (int i = 0; i < left.length(); i++) {
            if (left.charAt(i) == right.charAt(i)) {
                sameCount++;
            } else {
                break;
            }
        }
        return right.length() - sameCount;
    }


    public static void main(String[] args) {
        String[] strings = new String[50000000];
        int a = 0x4e00;
        int b = 0x9fa5;

        Random r = new Random(10);
        //Root Node
        long sum = 1;
        for (int i = 0; i < 50000000; i++) {
            int j = (int) (r.nextInt(4)) + 2;
            StringBuilder sb = new StringBuilder();
            for (int jj = 0; jj < j; jj++) {
                sb.append((char) (a + (int) (r.nextInt(b - a))));
            }
            strings[i] = sb.toString();
        }
        Arrays.sort(strings);

        sum += strings[0].length();
        for (int i = 1; i < 50000000; i++) {
            sum += differ(strings[i - 1], strings[i]);
        }
        System.out.println(sum);
    }
}
