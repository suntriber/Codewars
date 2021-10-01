package _7kyu;

import java.util.ArrayList;
import java.util.Arrays;

/*********************************************************************************************************************
 * In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice.
 * Your task will be to return the sum of the numbers that occur only once.
 *
 * For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
 * Every other number occurs twice.
 *
 * More examples in the test cases.
 *
 * Good luck!
 *
 *********************************************************************************************************************/
public class Sum_of_array_singles {

    public static void main(String[] args) {

        System.out.println(15 + ", " + repeats(new int[]{4, 5, 7, 5, 4, 8}));
        System.out.println(19 + ", " + repeats(new int[]{9, 10, 19, 13, 19, 13}));
        System.out.println(12 + ", " + repeats(new int[]{16, 0, 11, 4, 8, 16, 0, 11}));
    }

    public static int repeats(int[] arr) {
        boolean[] count = new boolean[arr.length];
        //Arrays.fill(count, false);
        for (int i = 0; i < arr.length; i++) {
            if (count[i]) continue;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    count[j] = true;
                    count[i] = true;
                }
            }
        }
        int total = 0;
        for (int i = 0; i < arr.length; i++) {
            if (!count[i]) total += arr[i];
        }
        return total;
    }
}
