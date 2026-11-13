import java.util.Scanner;

public class sum_array {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n;
        int sum;
        sum = 0;
        System.out.println("Enter the size of array:");
        n =sc.nextInt();
        int[] a=new int[n];
        System.out.println("Enter the array element:");
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();

        } 
        for(int i=0;i<n;i++){
            sum=sum+a[i];

        }
        System.out.println("Sum Of Array Element:" + sum);
        int avg=sum/n;
        System.out.println("Average :" + avg);
        

        
    }
    
}
