package _8kyu;

/*************************************************************
 * Complete the square sum function so that it squares each number
 * passed into it and then sums the results together.
 *
 * For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
 *************************************************************/

public class Square_n_Sum {

    public static void main(String[] args) {


       System.out.println(squareSum(new int[] {1,2,2}));
        System.out.println(squareSum(new int[] {1,2}));
        System.out.println(squareSum(new int[] {5,-3,4}));
    }

    public static int squareSum(int[] n)
    {
        int totalSum = 0;
        for (int i = 0; i < n.length; i++){
            totalSum += n[i]*n[i];
        }
        return totalSum;
    }
}
