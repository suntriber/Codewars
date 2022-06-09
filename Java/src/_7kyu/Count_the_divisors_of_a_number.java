package _7kyu;
/*
https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/java
 */
public class Count_the_divisors_of_a_number {

    public static void main(String[] args) {

        System.out.format("16 -> 8 [%d]\n", numberOfDivisors(30));

    }

    public static long numberOfDivisors(int n) {
        int divisors = 2;

        for (int i = 2; i < n; i++) {
        if (n % i == 0) divisors++;
    }

        return divisors;
}

}

