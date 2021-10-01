package se.hkr;

public class Exam {
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    /* function */
    int function(int arr[])
    {
        int n = arr.length;
        for (int g = n/2; g > 0; g /= 2)
        {
            for (int i = g; i < n; i += 1)
            {
                int temp = arr[i];
                int j;
                for (j = i; j >= g && arr[j - g] > temp; j -= g)
                    arr[j] = arr[j - g];
                arr[j] = temp;
            }
        }
        return 0;
    }

    public static void main(String args[])
    {
        int arr[] = {12, 34, 54, 2, 3, 17, 22, 51, 13, 28, 1, 24, 32, 7};
        System.out.println(" .....  ");
        printArray(arr);
        Exam ob = new Exam();
        ob.function(arr);
        System.out.println(" ...  ");
        printArray(arr);
    }

}
