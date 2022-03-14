package se.hkr;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] arr1 = {1,2,3,4};
        int[] arr2 = Arrays.copyOf(arr1, 8);
        int[] arr3 = Arrays.copyOf(arr2, 16);

        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
        System.out.println(Arrays.toString(arr3));
    }
}
